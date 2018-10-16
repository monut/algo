#!/usr/bin/env python
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

import sdrstats

import json
import time
import os
import sys
import numbers
import csv
import math
import socket
import urllib
import tempfile
import subprocess
import datetime
import re

import stats
import exhibit
import dygraph
import gnuplot
import topstats
import messages

collections =  dict()

def make_exhibit_html():
   dir = os.path.dirname(__file__)
   path = os.path.join(dir, "exhibit.html")
   with open(path) as f:
      return f.read()

class MyHandler(SimpleHTTPRequestHandler):
   def do_HEAD(s):
      s.send_response(200)
      s.send_header("Content-type", "text/html")
      s.end_headers()
   def do_GET(s):
      if s.path.startswith("/exhibit_json"):
         s.send_response(200)
         s.send_header("Content-type", "application/json")
         s.end_headers()
         s.wfile.write(exhibit.generate_exhibit_json(collections))
         return
      if s.path.startswith("/dygraph_csv?"):
         query = s.path[len("/dygraph_csv?"):]
         query = urllib.unquote(query)
         s.send_response(200)
         s.send_header("Content-type", "application/text")
         s.end_headers()
         source, sep, path = query.partition(":")
         stat = stats.get_item(collections[source], path)
         s.wfile.write(dygraph.generate_dygraph_csv(stat))
         return
      if s.path.startswith("/gnuplot?"):
         query = s.path[len("/gnuplot?"):]
         query = urllib.unquote(query)
         s.send_response(200)
         s.send_header("Content-type", "image/png")
         s.end_headers()
         source, sep, path = query.partition(":")
         stat = stats.get_item(collections[source], path)
         gnuplot.write_png(stat, s.wfile, title=path, legend=source)
         return
      if s.path == "" or s.path == "/":
         s.send_response(200)
         s.send_header("Content-type", "text/html")
         s.end_headers()
         s.wfile.write(make_exhibit_html())
         return
      if s.path.startswith("/__history__.html"):
         s.send_response(200)
         s.send_header("Content-type", "text/html")
         s.end_headers()
         s.wfile.write("<html><body></body></html>")
         return
      s.send_response(404)

def parse_sdr_stats(name, file, rules=None):
   if rules is not None:
      print "Running rules on %s" % name
      with tempfile.NamedTemporaryFile() as temp:
         args =["/u/jvanhoutte/bin/sdr-parser", "-s", file, "-o", temp.name,
               "-r", rules]
         subprocess.Popen(args).wait()
         print "Parsing %s" % name
         s = sdrstats.parse_stats(temp)
         s.source_ = name
         collections[name] = s
   else:
      print "Parsing %s" % name
      with open(file) as f:
         s = sdrstats.parse_stats(f)
         s.source_ = name
         collections[name] = s

def parse(name, file, rules):
   #sdr_names = ["sdr.stats", "sdr.stats.txt"]
   sdr_names = re.compile(r"sdr\.stats(\.[0-9]+)?(\.txt)?$")
   messages_names = re.compile(r"messages(\.([0-9]+)|(txt))?$")
   top_names = ["top.stats", "top.stats.txt"]
   if messages_names.match(os.path.basename(file)):
      print "Parsing counts from %s" % name
      with open(file) as fd:
         d = datetime.date.fromtimestamp(os.fstat(fd.fileno()).st_ctime)
         s = messages.parse_counts(fd, d.year)
         s.source_ = name
         collections[name] = s
      return True
   elif sdr_names.match(os.path.basename(file)):
      print "Parsing sdr stats %s" % name
      parse_sdr_stats(name, file, rules)
      return True
   elif os.path.basename(file) in top_names:
      print "Parsing top stats %s" % name
      with open(file) as fd:
         s = topstats.parse(fd)
      s.source_ = name
      collections[name] = s
      return True
   else:
      return False
if __name__ == '__main__':
   rules = "/u/jvanhoutte/bin/script-rules"
   if len(sys.argv) < 2:
      print "usage: %s [files to parse] [directories to search]" % sys.argv[0]
      print "parses stats files and serves and interative website to display them"
      sys.exit()
   for arg in sys.argv[1:]:
      if os.path.isfile(arg):
         r = parse(arg, arg, rules)
         if not r:
            print "unknown file type", arg
      else:
         root = arg
         for curroot, dirs, files in os.walk(root, followlinks=True):
            for f in files:
               path = os.path.join(curroot, f)
               name = os.path.relpath(path, root)
               parse(name, path, rules)
   server_class = BaseHTTPServer.HTTPServer
   server_class = BaseHTTPServer.HTTPServer
   httpd = server_class(("", 0), MyHandler)
   (host, port) = httpd.server_address
   host = socket.getfqdn()
   print "Server started - http://%s:%s/" % (host, port)
   try:
      httpd.serve_forever()
   except KeyboardInterrupt:
      pass
   httpd.server_close()
   print "Server stoped - %s:%s" % (host, port)

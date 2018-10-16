import sys
import stats

from datetime import datetime

class FormatError(Exception):
   pass

class Bucket:
   ranges = {}
   max = None
   def __repr__(self):
      return repr((self.ranges, self.max))

def num(s):
   try:
      return int(s)
   except ValueError:
      return float(s)

class SdrParser:

   date_prefix = "SDR Stats at ---- ----"
   path_prefix = "/"
   max_prefix = "  max: "
   date_format = "%a %b %d %H:%M:%S %Y"

   def __init__(self):
      self.date = None
      self.path = None
      self.bucket = None
      self.stats = stats.Collection("sdr")

   def parse_line(self, line):
      line = line[:-1]
      if line.startswith(self.date_prefix):
         self.parse_date(line)
      elif line.startswith(self.path_prefix):
         self.parse_stat(line)
      elif line.startswith(self.max_prefix):
         pass
#         self.parse_max(line)
      else:
         self.parse_other(line)

   def parse_date(self, line):
      self.date = datetime.strptime(line[len(self.date_prefix):], self.date_format)

   def parse_stat(self, line):
      [path, value] = line.rsplit(" ", 1)
      #self.path = tuple(path[1:].split("/"))
      self.path = path
      try:
         value = num(value)
         self.add_stat(value)
      except ValueError:
         pass
   def parse_max(self, line):
      value = line[len(self.max_prefix):]
      value, junk = value.split(" ", 1)
      if self.bucket is None:
         self.bucket = Bucket()
      self.bucket.max = num(value)
      self.add_stat(self.bucket)

   def parse_other(self, line):
      parts = line.split(":")
      if len(parts) != 2:
         return
      if self.bucket is None:
         self.bucket = Bucket()
      count = num(parts[0].strip())
      value = parts[1].strip()
      self.bucket.ranges[value] = count

   def add_stat(self, x):
      self.stats.add_value(self.path, self.date, x)
      self.bucket = None
      self.path = None


def parse_stats(fd):
   parser = SdrParser()
   for line in fd:
      parser.parse_line(line)
   return parser.stats


if __name__ == "__main__":
   with open(sys.argv[1]) as f:
      stats = parse_stats(f)

import math

def get_item(collection, path, delimiter="/"):
   name, sep, rest = path.partition(delimiter)
   if collection.name != name:
      raise ValueError()
   if rest == "":
      return collection
   else:
      return collection.get_item(rest, delimiter)

class Item:
   def __init__(self, name, parent, source=None):
      self.name = name
      self.parent = parent
      self.source_ = source

   def full_name(self, delimiter="/"):
      if self.parent is None:
         return self.name
      else:
         return self.parent.full_name(delimiter) + delimiter + self.name

   def source(self):
      if self.source_ is not None or self.parent is None:
         return self.source_
      else:
         return self.parent.source()

   def __repr__(self):
      return "Item(" + ", ".join([
         repr(self.name), repr(self.parent), repr(self.source_)]) + ")"

class Collection(Item):
   def __init__(self, name, parent=None, source=None):
      Item.__init__(self, name, parent, source)
      self.items = dict()

   def add_item(self, item):
      self.items[item.name] = item
      item.parent = self

   def add_value(self, path, date, value, delimiter="/"):
      print "HERE "
      if path[0] == delimiter:
         path = path[1:]
      name, sep, path = path.partition(delimiter)
      if path == "":
         if name not in self.items:
            self.items[name] = Stat(name, self)
         self.items[name].add_value(date, value)
      else:
         if name not in self.items:
            self.items[name] = Collection(name, self)
         print 'NAME:' + name
         print path
         print value
         self.items[name].add_value(path, date, value, delimiter)


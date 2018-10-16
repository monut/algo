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

   def all_stats(self, delimiter = "/"):
      for item in self.items.itervalues():
         if hasattr(item, "values"):
            yield (self.name, item)
         if hasattr(item, "all_stats"):
            for (path, stat) in item.all_stats(delimiter):
               yield (self.name + delimiter + path, stat)

   def all_items(self):
      for item in self.items.itervalues():
         yield item
         if hasattr(item, "all_items"):
            for child in item.all_items():
               yield child

   def get_item(self, path, delimiter="/"):
      name, sep, rest = path.partition(delimiter)
      if rest == "":
         return self.items[name]
      else:
         return self.items[name].get_item(rest, delimiter)


class Stat(Item):
   def __init__(self, name, parent):
      Item.__init__(self, name, parent)
      self.value_map = dict()

   def values(self):
      return self.value_map.itervalues()

   def number_values(self):
      for value in self.values():
         if not math.isnan(value):
            yield value

   def pairs(self):
      for date in sorted(self.value_map.iterkeys()):
         yield (date, self.value_map[date])

   def add_value(self, date, value):
      if date in self.value_map:
         return
         raise Exception("A value already exists for this date " + str(date)
               + " stat: " + self.full_name() +
               " exisiting: " + str(self.value_map[date]) +
               " new: " + str(value))
      self.value_map[date] = value

   def value_average(self):
      count = len([x for x in self.number_values()])
      if count == 0:
         return None
      return self.value_sum() / float(count)

   def value_maximum(self):
      try:
         return max(self.number_values())
      except ValueError:
         return None
   def value_minimum(self):
      try:
         return min(self.number_values())
      except ValueError:
         return None

   def value_sum(self):
      total = 0
      for value in self.number_values():
         total += value
      return total

   def value_count(self):
      return len(self.value_map)

   def nonzero(self):
      for number in self.number_values():
         if number != 0:
            return True
      return False

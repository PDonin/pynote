import types

a = "donin"
isinstance(a, str) #judge a
#judge the type of variable
print type(a)

type("abc") == types.StringType
# types.UnicodeType, types.IntType, types.ListType, types.TypeType,
type(int) == types.TypeType == type(str)

len("ABC") # == "ABC".__len__()

##############################
# class note
############################
class MyObject(object):
  def __init__(self, x):
    self.x = x
  def __len__(self):
    return 100

obj = MyObject(10)
print len(obj)
print hasattr(obj, 'x')
setattr(obj, 'x', 19)
print getattr(obj, 'x', 404) # if obj doesn't have x attr,return 404 instead

##############################
# class note2
############################
class Student(object):
  pass

s = Student()
s.name = "donin"
def set_age(self, age):
  self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s, Student) #bind a method to a object
s.set_age(15) # if you create a new object,it doesn't work

Student.set_age = MethodType(set_age, None, Student) #bind a method to a class


##############################
# class note3 ,use __slots__
############################
class People(object):
  __slots__ = ('name', 'age')
p = People()
p.name = "donin"
p.score = 100 #error,can't add score to object

##############################
# use @property
############################
class Employee(object):
  @property #getter
  def salary(self):
      return self._salary

  @salary.setter
  def salary(self, value):
    if not isinstance(value, int):
      rais ValueError("salary must be a integer")
    if value < 0 or value > 100000:
      raise ValueError("salary must between 0-1000000")
    self.score = value

##############################
# class note5 define your own class
############################
class Bird(object):
  def __init(self, name):
    self.name = name

  def __str__(self):
    return "Bird object (name: %s)", %self.name

  __repr__ = __str__

##############################
# if you want use for...in
############################
class Fib(object):
  def __init__(self):
    self.a, self.b = 0, 1

  def __iter__(self):
    return self

  def next(self):
    self.a, self.b = self.b, self.a + self.b
    if self.a > 10000:
      raise StopIteration();
    return self.a

for n in Fib():
  print n

##############################
# use class as a list
############################
class NewFib(object):
  def __getitem__(self, n):
    if isinstance(n, int):
      a, b = 1, 1
      for x in range(n):
        a, b = b, a + b
      return a
    if isinstance(n, slice):
      start = n.start
      stop = n.stop
      a, b = 1, 1
      L = []
      for x in range(stop):
        if x >= start:
          L.append(a)
        a, b = b, a + b
      return L
f = NewFib()
print f[2]
print f[0:5]

##############################
# __getattr__
############################
class Chain(object):
  def __init__(self, path = ''):
    self._path = path
  def __getattr__(self, path):
    return Chain('%s/%s' % (self._path, path))

  def __str__(self):
    return self._path

  def __call__(self, name):
    return Chain('GET %s/:%s' %(self._path, name))
print Chain().status.user.timeline.list
Chain().users('michael').repos #/users/:michael/repos
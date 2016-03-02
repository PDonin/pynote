import functools

def calc_sum(*args):
  sum = 0
  for n in args:
    sum += n
  return sum

# 9
def count():
  fs = []
  for i in range(1, 4):
    def f():
      return i * i
    fs.append(f)
  return fs

f1, f2, f3 = count()
# 
print f1(),f2(),f3()

def countR():
  fs = []
  for i in range(1,4):
    def f(j):
      def g():
        return j * j
      return g
    fs.append(f(i))
  return fs

fr1, fr2, fr3 = countR()
#
print fr1(),fr2(), fr3()

#########
map(lambda x: x * x, [1, 2, 3, 4, 5, 6])

f = lambda x : x * x
print f(5)

def build(x, y):
  return lambda: x * x + y * y

fun = build(10, 10)
print fun()


###############################
# decorator
##############################
def log(func):
  def wrapper(*args, **kw):
    print 'call %s()' % func.__name__
    return func(*args, **kw)
  return wrapper

@log # the same as now = log(now)
def now():
  print '2013-12-25'


print now()

def log2(text):
  def decorator(func):
    def wrapper(*args, **kw):
      print '%s %s()' %(text, func.__name__)
      return func(*args, **kw)
    return wrapper
  return decorator

@log2("execute") #the same as now2 = log("execute")(now2)
def now2():
  print '2016-3-2'

now2()

###############################################
# use functools
###############################################
def log3(func):
  @functools.wraps(func)
  def wrapper(*args, **kw):
    print 'call %s():' % func.__name__
    return func(*argc, **kw)
  return wrapper

def log4(text):
  def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
      print '%s %s():' %(text, func.__name__)
      return func(*args, **kw)
    return wrapper
  return decorator

# callable to judge a var is callable

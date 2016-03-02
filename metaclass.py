class Hello(object):
  def hello(self, name = 'world'):
    print 'Hello, %s' % name

h = Hello()

print type(h)
print type(Hello)

def fn(self, name = 'world'):
  print 'Hello, %s' % name

Hello = type('Hello', (object, ), dict(hello = fn)) #create a class Hello

#####################################################
#use type to create class dynamic
###################################################
class ListMetaclass(type):
  def __new__(cls, name, bases, attrs):
    attrs['add'] = lambda self, value: self.append(value)
    return type.__new__(cls, name, bases, attrs)

class MyList(list):
  __metaclass__ = ListMetaclass
  
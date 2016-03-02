import logging
try:
  r = 10 / 0
  print r
except ZeroDivisionError, e:
  logging.exception(e)
finally: #always run 
  print '---'

class FooError(StandardError):
  pass

raise FooError('invalid value: %s' %s)


# if raise don't carry any paramter,it's just throw the error before


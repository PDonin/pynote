'''
with open('error.py', 'r') as f:
  # print f.read() #f.read(size)
  for line in f.readlines():
    print line.strip()
'''
'''
#binary file
with open('error.py', 'rb') as f:
  print f.read()
'''

'''
#open gbk file
import codecs
with codecs.open('gbk.txt', 'r', 'gbk') as f:
  f.read()
'''

'''
with open('log.txt', 'w') as f:
  f.write("hello world")
  f.close()
'''
import os
print os.path.abspath('.')
print os.path.join('Users/ecloud', 'testdir')
os.mkdir(os.path.join('Users/ecloud', 'testdir'))
os.rmdir(os.path.join('Users/ecloud', 'testdir'))

os.path.split('/Users/ecloud/testdir/file.txt') # ('/Users/ecloud/testdir', 'file.txt')

os.path.splitext('path/to/file.txt') # ('path/to/file', '.txt')

os.rename('text.txt', 'test.py')

os.remove('test.py')

[x for x in os.listdir('.') if os.path.]

# coding=utf-8

'''
Created on 2017年8月21日
 
@author: THINK
'''


import os
# import os.path
print os.path.abspath('.')

os.path.join(os.path.abspath('.'), 'libtest')
print os.path.split('/Users/michael/testdir/file.txt')
print os.listdir('..')
print os.listdir('.')
print  (x for x in os.listdir('.') if os.path.isdir(x))
print  [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
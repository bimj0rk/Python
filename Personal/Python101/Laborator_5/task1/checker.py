#!/usr/bin/python3
import json
from task1_1 import student_function as task1_1
from task1_2 import student_function as task1_2

# import BeautifulSoup

print ('****************  TASK 01  *********************')

print ('TASK 1.1:')
task1_out = task1_1()
test1 = open('test1.txt', 'r')
task1_ref = test1.read()
test1.close()

try:
    assert str(task1_out) == task1_ref
    print ("SUCCESS.................. 1p/1p")
except:
    print ("FAILED\n")

print ('TASK 1.2:')
task2_out = task1_2()
test2 = open('test2.txt', 'r')
task2_ref = test2.read()
test2.close()

try:
    assert str(task2_out) == task2_ref
    print ("SUCCESS.................. 1p/1p\n")
except:
    print ("FAILED\n")
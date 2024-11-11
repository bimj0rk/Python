#!/usr/bin/python3
import json
from task2_0 import student_function as task2_0
from task2_1 import student_function as task2_1
from task2_2 import student_function as task2_2
from task2_3 import student_function as task2_3


print ('****************  TASK 02  *********************')

print ('TASK 2.0:')
task0_out = task2_0()
test0 = open('test0.txt', 'r')
task0_ref = test0.read()
test0.close()
try:
    assert str(task0_out) == task0_ref
    print ("SUCCESS.................. 1p/1p")
except:
    print ("FAILED\n")

print ('TASK 2.1:')
task1_out = task2_1()
test1 = open('test1.txt', 'r')
task1_ref = test1.read()
test1.close()
try:
    assert str(task1_out) == task1_ref
    print ("SUCCESS.................. 1p/1p")
except:
    print(str(task1_out))
    print ("FAILED\n")

print ('TASK 2.2:')
task2_out = task2_2()
test2 = open('test2.txt', 'r')
task2_ref = test2.read()
test2.close()
try:
    assert str(task2_out) == task2_ref
    print ("SUCCESS.................. 1p/1p")
except:
    print ("FAILED\n")

print ('TASK 2.3:')
task3 = open('output.csv', 'w')
task2_3(task3)
task3.close()
task3 = open('output.csv', 'r')
task3_out = task3.read()
test3 = open('test3.csv', 'r')
task3_ref = test3.read()
test3.close()
try:
    assert task3_out == task3_ref
    print ("SUCCESS.................. 1p/1p")
except:
    print ("FAILED\n")
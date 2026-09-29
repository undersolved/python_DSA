import sys

sys.stdin = open('demo/input.txt','r') #noqa
sys.stdout = open('demo/output.txt','w') #noqa

num1 = int(input("Enter the number"))
num2 = int(input("Enter the second number"))

print( num1 + num2)
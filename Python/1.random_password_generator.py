# RANDOM PASSWORD GENERATOR 
import random
char_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+'
input_length = int(input('Enter the length : '))
password = ''
for i in range(1,input_length+1):
    password += random.choice(char_list)
print(password)    
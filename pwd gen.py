import random
import string

all_char = string.ascii_letters+string.digits+string.punctuation
print("Welcome in Password generator ")
pwd_length = int(input("Please enter your length of password:"))
pwd=""

for i in range(pwd_length):
    pwd += random.choice(all_char)

print(" Your random Password is {}" .format(pwd))
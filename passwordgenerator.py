import random

password = ""

for i in range(8):
    password += chr(random.randint(33, 126))
print(password)
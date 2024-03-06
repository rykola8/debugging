# Mērķis: 
# uzģenerēt paroli no burtiem un cipariem noteiktā garumā

password_length = int(input("Kāds būs garums?"))
import random
import string
password = ""
for i in range(password_length):
    if i % 2 == 0:
        password += str(random.randint(0, 9))
    else:
        password += random.choice(string.ascii_letters)

print("Jauna parole:", password)

# Kādas kļūdas izdevies atrast?
# 

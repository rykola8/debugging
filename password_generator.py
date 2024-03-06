# Mērķis: 
# uzģenerēt paroli no burtiem un cipariem noteiktā garumā

password_length = input("Kāds būs garums?")

password = ""
for i in range(12):
if i % 2 == 0:
passwrd += str(random.randint(0, 9))
else
password += randm.choice(string.ascii_letters)

print("Jauna parole:", password)

# Kādas kļūdas izdevies atrast?
# 

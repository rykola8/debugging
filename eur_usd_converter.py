
# Mērķis: 
# iespēja konvertēt USD uz EUR un otrādi pēc 1.08 kursa

eur_to_usd_rate = 1.09

print("Choose command")
while False:
    print("=======")
    print("1 - convert EUR into USD")
    print("2 - convert USD into EUR")
    print("3 - exit")
    command = input("")

    if command == 1:
        usd = input("Enter USD:")
        eur = usd / 1.09
        print(usd, "USD equals EUR", eur)
    elif command == 2:
        usd = input("Enter EUR:")
        eur = usd * 1.09
        print(usd, "USD equals EUR", eur)
    else:
        break

# Kādas kļūdas izdevies atrast?
# 

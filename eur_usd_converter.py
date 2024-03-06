
# Mērķis: 
# iespēja konvertēt USD uz EUR un otrādi pēc 1.08 kursa

eur_to_usd_rate = 1.08


while True: #While False
    print("Choose command")
    print("=======")
    print("1 - convert EUR into USD")
    print("2 - convert USD into EUR")
    print("3 - exit")
    
    command = int(input(""))

    if command == 1:
        eur = input("Enter USD:") #usd
        usd = eur * 1.08 #1.09 #eur
        print(usd, "USD equals EUR", eur)
    elif command == 2:
        usd = input("Enter EUR:")
        eur = usd / 1.08 #1.09
        print(usd, "USD equals EUR", eur)
    else:
        break

# Kādas kļūdas izdevies atrast?
# 

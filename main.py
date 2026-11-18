import random
val=["sten", "sax", "påse"]
Spelarens_Poäng = 0
Datorns_Poäng = 0

print ("Nu ska vi spela Sten, Sax eller Påse!")
print ("Jag är en robot")
print ()
Spelar_namn = input("Vad ska jag kalla dig --> ")
while True:

    try:
        Antal_omgångar = int(input ("Hur många antal omgångar ska vi spela? -->"))
        break
    except ValueError:
        continue

print ()

for i in range(Antal_omgångar):
    print ("spelomgång" , i+1)
    print ("---------------------")
    Användarens_val = (input("Välj Sten, Sax eller Påse -->"))

    while (Användarens_val) not in val:
        print ("Ogiltig inmatning")
        (Användarens_val) = (input("Välj Sten, Sax eller Påse -->"))

    datorns_val=random.choice(val)
    print ()
    print ("Python 311 spelar:",datorns_val)
    print (Spelar_namn,"spelar:",Användarens_val)

    if (datorns_val) == (Användarens_val):
        print ("Det blev oavgjort")
    elif (datorns_val) == "sten" and (Användarens_val) == "sax":
        print ("Du förlorade :(")
        (Datorns_Poäng)= (Datorns_Poäng)+1
    elif (datorns_val) == "sax" and (Användarens_val) == "påse":
        print ("Du förlorade")
        (Datorns_Poäng)= (Datorns_Poäng)+1
    elif (datorns_val) == "påse" and (Användarens_val) == "sten":
        print ("Du förlorade")
        (Datorns_Poäng)= (Datorns_Poäng)+1
    else:
        print ("Du vann!")
        (Spelarens_Poäng) = (Spelarens_Poäng) +1
    print (Spelar_namn,Spelarens_Poäng)
    print ("Roboten",Datorns_Poäng)
    
    if i == (Antal_omgångar-1):
        if Spelarens_Poäng > Datorns_Poäng:
            print ("Du är vinnaren!")
            print ()
        elif Datorns_Poäng == Datorns_Poäng:
             print ("Det blev oavgjort")
             print ()
        else:
            print ("Roboten vann")
    

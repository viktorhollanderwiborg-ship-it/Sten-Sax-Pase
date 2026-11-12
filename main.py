import random
val=["sten", "sax", "påse"]
Spelarens_Poäng = 0
Datorns_Poäng = 0

print ("Nu ska vi spela Sten, Sax eller Påse!")
print ("Jag är en robot")
print ()
Spelar_namn = input("Vad ska jag kalla dig --> ")
Antal_omgångar = input ("Hur många antal omgångar ska vi spela? -->")

print ()

for i in range (Antal_omgångar):
    print ("spelomgång" , i+1)
    print ("---------------------")
    Användarens_val = (input("Välj Sten, Sax eller Påse -->"))

    while (Användarens_val) not in val:
        print ("Ogiltig inmatning")
        (Användarens_val) = (input("Välj Sten, Sax eller Påse -->"))

    datorns_val=random.choice(val)
    print ("datorn valde",datorns_val)

    if (datorns_val) == (Användarens_val):
        print ("Det blev oavgjort :/")
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
        print ("Du vann! :D")
        (Spelarens_Poäng) = (Spelarens_Poäng) +1
    print (Spelar_namn,Spelarens_Poäng)
    print ("Roboten",Datorns_Poäng)
    print ()
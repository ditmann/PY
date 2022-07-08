#kalkulator

def addere(x,y):
    return x + y

def subtrahere(x,y):
    return x - y

def multiplisere(x,y):
    return x * y

def dividere(x,y):
    return x / y


print("Hva skal jeg gjøre?  ")
print("1.addere")
print("2.subtrahere")
print("3.multiplisere")
print("4.dividere")

while True:
    valg = input("Velg 1, 2, 3 eller 4  ")


    if valg in ('1','2','3','4'):
        nr1 = float (input ("tall nr1:  "))
        nr2 = float (input ("tall nr2:  "))
   

        if valg == "1":
            print(nr1, "+", nr2, "=", addere(nr1, nr2))

        elif valg =="2":
            print(nr1, "-", nr2, "=", subtrahere(nr1, nr2))
    
        elif valg =="3":
            print(nr1, "x", nr2, "=", multiplisere(nr1, nr2))
    
        elif valg =="4":
          print(nr1, "/", nr2, "=", dividere(nr1, nr2))

        neste = input ("neste? (y/n) ")
        if neste == "n":
            break

    else:
        print("nå må du slutte og tulle")
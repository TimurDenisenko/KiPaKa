from random import *
from getpass import *
from time import * 

gameElem=["Kivi","Paber","Käärid"]

vali=input("Kas sa tahad mängida võistlusrežiimile? (jah või ei) ").lower()
while vali not in ["jah","ei"]:
    vali=input("Kirjuta ainult jah või ei! ").lower()

if vali=="jah":

    n1=[]
    n2=[]
    n3=[]
    n4=[]
    Tn1=[]
    Tn2=[]
    Tn3=[]
    Tn4=[]

    n=input("Mitu võistlust me mängime? Mitte rohkem kui 4 korda ")
    while n.isdigit()==False or int(n)>4 or int(n)<2:
        n=input("Kirjuta õige arv! ")

else:
    n=1

ma=vi=ka=vo=vi1=ka1=vo1=nimi2=0
n=int(n)

game=input("Kas tahad mängida kellegagi-(2) või robotiga-(1) ")
while game not in ["1","2"]:
    game=input("Palun kirjuta 1 või 2 ")

for p in range(n): 

    IV=IK=II=RV=RK=RI=0
    võidudI=[]
    võidudR=[]

    if game=="1" and p==0:

        nimi1=input("Mis sinu nimi on? ").title()


    elif game=="2" and p==0:

        nimi1=input("Esimene inimene mis sinu nimi on? ")
        while nimi1.isalpha()==False or len(nimi1)<2:
            nimi1=input("Palun kirjuta õige nimi! ").title()

        nimi2=input("Teine inimene, mis sinu nimi on? ").title()
        while nimi2.isalpha()==False or len(nimi2)<2:
            nimi2=input("Palun kirjuta õige nimi! ").title()


    mäng=input("Mitu korda sa tahad mängida? Mitte rohkem kui 5 korda ")
    while mäng.isdigit()==False or int(mäng)>5 or int(mäng)==0:
        mäng=input("Kirjuta õige arv! ")
    mäng=int(mäng)

    if game=="1":
        nimi3="Robot"

        for i in range(int(mäng)):

            shuffle(gameElem)
            robot=gameElem[randint(0,2)]

            inimene=input(f"{nimi1} palun vali {gameElem} ").title()
            while inimene not in gameElem:
                inimene=input(f"{nimi1} palun kirjuta õige element {gameElem} ").title()

            for x in range(1,4):
                print(f"{x}...")
                sleep(1)

            if gameElem.index(inimene)<gameElem.index(robot):
                print(f"{nimi1}, sa võitsid!")
                võidudI.append(f"{i+1} robotimäng - võit")
                IV+=1
                võidudR.append(f"{i+1} robotimäng - kaotus")
                RK+=1

            elif gameElem.index(inimene)>gameElem.index(robot):
                print(f"{nimi1}, sa kaotasid!")
                võidudR.append(f"{i+1} robotimäng - võit")
                RV+=1
                võidudI.append(f"{i+1} robotimäng - kaotus")
                IK+=1

            else:
                print(f"{nimi1}, sul on viik!")
                võidudI.append(f"{i+1} robotimäng - viik")
                II+=1
                võidudR.append(f"{i+1} robotimäng - viik")
                RI+=1
                

            if p+1==1:
                n1.insert(i,võidudI[i])
                Tn1.insert(i,võidudR[i])

            elif p+1==2:
                n2.insert(i,võidudI[i])
                Tn2.insert(i,võidudR[i])

            elif p+1==3:
                n3.insert(i,võidudI[i])
                Tn3.insert(i,võidudR[i])

            elif p+1==4:
                n4.insert(i,võidudI[i])
                Tn4.insert(i,võidudR[i])

            print()

        ma+=mäng
        ka+=IK
        ka1+=RK 
        vo+=IV 
        vo1+=RV 
        vi+=II 
        vi1+=RI 

        print(f"{nimi1}:")
        print(võidudI)
        print(f"Mängude arv - {mäng}\nVõidud - {IV}\nKaotused - {IK}\nViik - {II}")

        print()

        print(f"{nimi3}:")
        print(võidudR)
        print(f"Mängude arv - {mäng}\nVõidud - {RV}\nKaotused - {RK}\nViik - {RI}")

        print()

    else:
        for i in range(mäng):

            shuffle(gameElem)
            print("Sisestatud tekst ei ole mängu huvides nähtav!")
            sleep(1)


            EsInimene=getpass(f"{nimi1}, palun vali {gameElem} ").title()
            while EsInimene not in gameElem:
                EsInimene=getpass(f"{nimi1}, palun kirjuta õige element {gameElem} ").title()

            TeInimene=getpass(f"{nimi2}, palun vali {gameElem} ").title()
            while TeInimene not in gameElem:
                TeInimene=getpass(f"{nimi2}, palun kirjuta õige element {gameElem} ").title()


            sleep(1)
            for x in range(1,4):
                print(f"{x}...")
                sleep(1)


            if gameElem.index(EsInimene)<gameElem.index(TeInimene):
                print(f"{nimi1}, sa võitsid!")
                print(f"{nimi2}, sa kaotasid!")
                võidudI.append(f"{i+1} TeInimeneimäng - võit")
                IV+=1
                võidudR.append(f"{i+1} TeInimeneimäng - kaotus")
                RK+=1

            elif gameElem.index(EsInimene)>gameElem.index(TeInimene):
                print(f"{nimi2}, sa võitsid!")
                print(f"{nimi1}, sa kaotasid!")
                võidudR.append(f"{i+1} TeInimeneimäng - võit")
                RV+=1
                võidudI.append(f"{i+1} TeInimeneimäng - kaotus")
                IK+=1

            else:
                print(f"{nimi1} ja {nimi2}, teil on viik!")
                võidudI.append(f"{i+1} TeInimeneimäng - viik")
                II+=1
                võidudR.append(f"{i+1} TeInimeneimäng - viik")
                RI+=1


            if p+1==1:
                n1.insert(i,võidudI[i])
                Tn1.insert(i,võidudR[i])

            elif p+1==2:
                n2.insert(i,võidudI[i])
                Tn2.insert(i,võidudR[i])

            elif p+1==3:
                n3.insert(i,võidudI[i])
                Tn3.insert(i,võidudR[i])

            elif p+1==4:
                n4.insert(i,võidudI[i])
                Tn4.insert(i,võidudR[i])

            print()

        ma+=mäng
        ka+=IK
        ka1+=RK 
        vo+=IV 
        vo1+=RV 
        vi+=II 
        vi1+=RI 

        print(f"{nimi1}:")
        print(võidudI)
        print(f"Mängude arv - {mäng}\nVõidud - {IV}\nKaotused - {IK}\nViik - {II}")

        print()

        print(f"{nimi2}:")
        print(võidudR)
        print(f"Mängude arv - {mäng}\nVõidud - {RV}\nKaotused - {RK}\nViik - {RI}")

        print()

print()
print()

if n!=1:
    print("Võistluse tulemuse kuvamine..")
    for l in range(3):
        sleep(1)
        print("."*(l+1))
    sleep(1)
    print()

    print(f"{nimi1}:")

    print(f"Esimene mäng\n{n1}")
    sleep(1)

    if n>=2:
        print(f"Teine mäng\n{n2}")
        sleep(1)

        if n>=3:
            print(f"Kolmas mäng\n{n3}")
            sleep(1)

            if n==4:
                print(f"Neljas mäng\n{n4}")
                sleep(1)

    print(f"Mängude arv - {ma}\nVõidud - {vo}\nKaotused - {ka}\nViik - {vi}")

    sleep(1)
    print()

    if nimi2!=0:
        print(f"{nimi2}:")
    else:
        print(f"{nimi3}:")

    print(f"Esimene mäng\n{Tn1}")
    sleep(1)

    if n>=2:
        print(f"Teine mäng\n{Tn2}")
        sleep(1)

        if n>=3:
            print(f"Kolmas mäng\n{Tn3}")
            sleep(1)

            if n==4:
                print(f"Neljas mäng\n{Tn4}")
                sleep(1)

    print(f"Mängude arv - {ma}\nVõidud - {vo1}\nKaotused - {ka1}\nViik - {vi1}")

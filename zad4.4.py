import random
a="Nigdy nie rezygnuj z celu tylko dlatego, że osiągnięcie go wymaga czasu. Czas i tak upłynie."
b="Sukces to drabina, po której nie sposób wspiąć się z rękami w kieszeniach."
c="Pomysły są powszechnym towarem. Wprowadzanie ich w życie nie jest."
d="W dwa miesiące możesz zdobyć więcej przyjaciół, interesując się innymi ludźmi, niż w ciągu dwóch lat, usiłując zainteresować sobą innych."
e="Zrób to, zanim będziesz gotów, gdyż nigdy nie będziesz gotów, jeśli będziesz czekać."
f="Kto nie chce, kiedy może, ten nie będzie mógł, kiedy będzie chciał."
g="Nic nie jest szczególnie trudne do zrobienia, jeśli tylko rozłożyć to na etapy."
h="Zacznij od robienia tego, co konieczne; potem zrób to, co możliwe; nagle odkryjesz, że dokonałeś niemożliwego."
i="Nie martw się porażkami, martw się szansami, które tracisz, gdy nawet nie próbujesz."
j="Umysły są jak spadochrony – działają tylko gdy są otwarte."
osoby=int(input("Podaj liczbę osób, które chcą poznać swoje motto na dziś: "))
for i in range(osoby):
    imie=input("Wpisz imię: ")
    los=random.randint(1,10)
    if los==1:
        los=a
    elif los==2:
        los=b
    elif los==3:
        los=c
    elif los==4:
        los=d
    elif los==5:
        los=e
    elif los==6:
        los=f
    elif los==7:
        los=g
    elif los==8:
        los=h
    elif los==9:
        los=i
    elif los==10:
        los=j
    print(imie,"Twoje motto na dziś to'",los,"'")
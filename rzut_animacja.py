import matplotlib.pylab as plt
import numpy as np
import math
from matplotlib.animation import FuncAnimation

# nasz program bedzie się rozwijał z czasem o nowe przypadki tak by obiąć jak najszerszy zakres wszelkich rzutów

# oznaczenia:
g = 9.81  # można zmienic jak coś narazie jako stała w [m/s^2]
Vgr = 8000      #predkosc gazow wyrzucanych z rakiety
G = 6.7*(10**(-11))
Mz = 6*(10**24)      #[kg]
Rz = 6371000         #[m]
V1 = np.around(np.sqrt((G*Mz)/Rz), 1) #[m/s]
V2 = np.around((np.sqrt(2) * V1), 1)
x = []
y = []

def skladowe (kat,pirewotna):                    #progra liczący skłodwe wektorów
    sinalf = np.around(np.sin(np.deg2rad(kat)),4)
    cosalf = np.around(np.cos(np.deg2rad(kat)),4)
    skłX = np.around(pirewotna * cosalf,4)
    skłY = np.around(pirewotna * sinalf,4)
    print('składowa wartosc poczatkowej wzdluz x:', skłX \
            , 'składowa wartosc poczatkowej wzdluz y:', skłY)
    return [skłX,skłY]


def CzasLotu(g, Vox, Voy, h, beta):
    # x = Vox * t  ==>  t = x/Vox
    # y = h + Voy*t - (g*t^2)/2  ==>  y = h + (Voy/Vox)*x - (g*x^2)/2*Vox^2
    # y = tg(beta)*t  ==>  y = tg(beta)/Vox * x - ODW*tg(beta)
    # -(g*x^2)/2*Vox^2 + (Voy/Vox - tg(beta)/Vox) * x + h = 0
    if Vox == 0:
        t = np.around(2 * Voy/g, 4)
        return t
    else:
        a = - g / (2 * (Vox**2))
        b = Voy/Vox - (np.tan(np.deg2rad(beta)) / Vox)
        c = h + ODW*np.tan(np.deg2rad(beta))
        delta = (b * b) - 4 * a * c
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        if x1 >= x2:
            t = np.around(x1/Vox, 4)
        else:
            t = np.around(x2/Vox, 4)
        print('Czas lotu wynosi t =', t)
        return (t)


def MaxWysokosc(Voy, g):  # program liczacy maksymalna wysokosc ciała
    H = np.around((Voy ** 2) / (2 * g), 4)
    Hmax = H + h
    print('maksymalna wysokosc na jaka wzleci cialo to H =', Hmax, 'm')
    return (Hmax)


def Zasieg(Vox, tc):
    z = np.around(Vox * tc, 4)
    print('Zasieg rzutu to z =', z, 'm')
    return (z)

def PredkosciChwilowe(tc, Vox, Voy, g, h):
    global x
    global y
    i = 0
    t = 0
    while t < tc:
        Vx = Vox
        Vy = Voy - g * t
        if i >= 1:
            x.append(Vx * t)
            y.append(y[i-1] + Vy * dt)
        else:
            x.append(Vx * t)
            y.append(h + Vy * t)
        dt = 0.1
        t = t + dt
        i += 1
    return x, y

def Rakieta(Vgr):
    print("Czy chcesz sie dowiedziec jaka jest I predkosc kosmiczna dla ziemi?")
    wybor = str.upper(input("Wpisz TAK lub NIE:    "))
    print("I predkosc kosmiczna dla ziemi wynosi ", V1," Teraz sprobuj dopasowac parametry rakiety tak aby ja uzyskala")

    if wybor == "TAK":
        while True:
            m = input("podaj mase ciala: ")
            try:
                m = float(m)
                if m > 0:
                    break
                else:
                    print("Masa musi byc wyrazona w postaci liczby dodatniej")
            except:
                print("Masa musi byc wyrazona w postaci liczby dodatniej")

        while True:
            a = input("Podaj tempo utraty masy (spalania paliwa): ")
            try:
                a = float(a)
                if a > 0:
                    break
                else:
                    print("Tempo utraty masy musi byc liczba dodatnia")
            except:
                print("Tempo utraty masy musi byc liczba dodatnia")

        t = 0
        while (a*t) <= 3*m/4:
            Vr = np.around(Vgr * np.log(m/(m - a * t)), 1)
            t += 0.5
            if Vr >= V1:
                print("Rakieta osiagnela I predkosc kosmiczna i moze pozostac na orbicie ziemi")
                return Vr
        print("Rakieta nie osiagnela I predkosci kosmicznej")

def InnePlanety(G, Mz, Rz):
    planety = {}
    odp = "TAK"
    print("Program oblicza I predkosc kosmiczna dla roznych planet. Predkosc jest podana w m/s.")
    while odp == "TAK":
        nazwa = input("Wprowadz nazwe planety: ")
        x = float(input("Masa planety. Wprowadz liczbe przez ktora ma zostac przemnozona masa ziemi: "))
        y = float(input("Promien planety. Wprowadz liczbe przez ktora ma zostac przemnozony promien ziemi: "))
        mp = x * Mz
        rp = y * Rz
        v = np.around(np.sqrt((G * mp) / rp), 4)
        planety[nazwa] = v
        print(planety)
        odp = str.upper(input("Czy chcesz dodac kolejna planete, wpisz TAK lub NIE: "))
        if odp != "TAK":
            break
    return planety

print('Witaj!!!!')
while True:
    h = input('Z jakiej wysokości rzucic. h = ')
    try:
        h = float(h)
        if h > 0:
            break
        else:
            print("Wysokosc musi byc licba wieksza lub rowna zero")
    except:
        print("To nie jest liczba. Podaj liczbe!!")

while True:
    alfa = input('Pod jakim kątem do poziomu rzut ma zostać wykonany. alfa = ')
    try:
        alfa = float(alfa)
        if alfa >= 0 and alfa <= 90:
            break
        else:
            print("Kat alfa musi byc z przedzialu [0, 90]")
    except:
        print("To nie jest liczba. Podaj liczbe!!")

while True:
    Vo = input('Jaka ma byc prędkość początkowa obiektu Vo = ')
    try:
        Vo = float(Vo)
        if Vo > 0:
            break
        else:
            print("Predkosc musi byc liczba dodatnia")
    except:
        print("To nie jest liczba. Podaj liczbe!!")

print("""
        Jak ma wygladac podloze?
        0 - podłoże nie idzie w góre ani w dół
        1 - podłoże idzie w górę pod kątem beta do poziomu
        2 - podłoże idzie w dół pod kątem beta do poziomu
           """)

while True:
    wybor = input('Twój wybór to: ')
    if wybor == "0":
        beta = 0
        ODW = 0
        break
    elif wybor == "1":
        while True:
            beta = input('Kąt beta ma wynosić beta = ')
            try:
                beta = float(beta)
                if beta > 0 and beta < 90:
                    break
                else:
                    print("Kat beta musi byc z przedzialu (0, 90)")
            except:
                print("To nie jest liczba. Podaj liczbe!!")

        while True:
            ODW = input('Po ilu metrach podloze ma zaczac sie podnosic: ')
            try:
                ODW = float(ODW)
                if ODW >= 0:
                    break
                else:
                    print("To nie moze byc liczba ujemna")
            except:
                print("To nie jest liczba. Podaj liczbe!!")
        break
    elif wybor == "2":
        while True:
            beta = input('Kąt beta ma wynosić beta = ')
            try:
                beta = float(beta)
                if beta > 0 and beta < 90:
                    beta = 180 - beta
                    break
                else:
                    print("Kat beta musi byc z przedzialu (0, 90)")
            except:
                print("To nie jest liczba. Podaj liczbe!!")

        while True:
            ODW = input('Po ilu metrach podloze ma zaczac sie obnizac: ')
            try:
                ODW = float(ODW)
                if ODW >= 0:
                    break
                else:
                    print("To musi byc liczba dodatnia")
            except:
                print("To nie jest liczba. Podaj liczbe!!")
        break
    else:
        print('Błąd nie ma takiego wyboru!!!')

Vox, Voy = skladowe(alfa, Vo)
tc = CzasLotu(g,Vox,Voy,h,beta)
Hmax = MaxWysokosc(Voy, g)
z = Zasieg(Vox, tc)
PredkosciChwilowe(tc,Vox,Voy,g,h)

plt.plot(x, y)
plt.title("Wykres rzutu")
plt.show()

Rakieta(Vgr)
InnePlanety(G, Mz, Rz)

fig, ax = plt.subplots()
ax.set_xlim(0, z+1)
ax.set_ylim(0, Hmax +1)
line, = ax.plot(0,0)
x_pierwsze = []
y_pierwsze = []


def animacja_funkcaja(i):
    x_pierwsze.append(x[i])
    y_pierwsze.append(y[i])

    line.set_xdata(x_pierwsze)
    line.set_ydata(y_pierwsze)
    print(x_pierwsze)
    return line,

animacja = FuncAnimation(fig,func=animacja_funkcaja,frames=len(x)+1,interval=1)
plt.show()

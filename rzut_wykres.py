import matplotlib.pylab as plt
import numpy as np
import math

# nasz program bedzie się rozwijał z czasem o nowe przypadki tak by obiąć jak najszerszy zakres wszelkich rzutów
# część interakcyjna z użytkownikeim jest zaplanowana na późniejsze terminy więc narazie przyjmiemy sobie pewne sałe

# oznaczenia:
g = 9.81  # można zmienic jak coś narazie jako stała w [m/s^2]
h = 1.0  # wysokość z jakie rozpoczynamy rzut [m]
Vo = 20  # prędkość początkowa [m/s]
alfa = 60  # kąt nachylenia wektora Vo od poziomu w stopniach ustalić przdział
x = 0.0  # odległość od początku rzuty
y = 0.0  # wysokość od cała od pionu
tc = 0.0  # calkowity czas lotu
H = 0.0  # maksymalna wysokosc ns jaka wzniesie sie cialo od wysokosci poczatkowej
Hmax = 0.0  # maksymalna wysokosc na jaka wzniesie sie cialo
z = 0.0  # zasieg rzutu
t = 0.0
Vgr = 8000      #predkosc gazow wyrzucanych z rakiety
a = 5     #tempo utraty masy
m = 250
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

def CzasLotu(Voy, g, wybor):  # program liczacy calkowity czas lotu
    # y = h + Voy*t - 1/2*g*t^2  oraz y = tg(beta)*t
    # po kilku przekształceniach otrzymamy h + t*(Voy - tg(beta)) - 1/2*g*t^2 = 0
    # znajdujemy pierwiastki funkcji kwadratowej
    a = -g / 2
    b = Voy - np.tan(np.deg2rad(beta))
    c = h
    delta = (b * b) - 4 * a * c
    t1 = (-b - math.sqrt(delta)) / (2 * a)
    t2 = (-b + math.sqrt(delta)) / (2 * a)
    if t1 >= t2:
        t = np.around(t1, 4)
    else:
        t = np.around(t2, 4)
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

def PredkosciChwilowe(tc, Vox, Voy, g,t,Hmax,h):
    global x
    global y
    i = 0
    while t <= tc:
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
    print(x)
    print(y)
    return x, y

def Rakieta(m, a, t, Vgr):
    print("Rakieta")
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
    return planety

print('Witaj!!!!')
h = float(input('Z jakiej wysokości rzucic h = '))
alfa = float(input('Pod jakim kątem do poziomu rzut ma zostać wykonany alfa = '))
Vo = float(input('Jaka ma byc prędkość początkowa obiektu Vo = '))
print("""
        0 - podłoże nie idzie w góre ani w dół
        1 - podłoże idzie w górę pod kątem beta do poziomu
        2 - podłoże idzie w dół pod kątem beta do poziomu
           """)
wybor = int(input('Twój wybór to: '))
if wybor == 0:
    beta = 0
elif wybor == 1:
    beta = float(input('Kąt beta ma wynosić beta = '))
elif wybor == 2:
    beta = float(input('Kąt beta ma wynosić beta = '))
    beta = 180 - beta
else:
    print('Błąd nie ma takiego wyboru!!!')

Vox, Voy = skladowe(alfa, Vo)
tc = CzasLotu(Voy, g, wybor)
Hmax = MaxWysokosc(Voy, g)
z = Zasieg(Vox, tc)
PredkosciChwilowe(tc,Vox,Voy,g,t,Hmax,h)

plt.plot(x, y)
plt.title("Wykres rzutu")
plt.show()
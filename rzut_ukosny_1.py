import matplotlib.pylab as plt
import numpy as np
import math
# nasz program bedzie się rozwijał z czasem o nowe przypadki tak by obiąć jak najszerszy zakres wszelkich rzutów
# część interakcyjna z użytkownikeim jest zaplanowana na późniejsze terminy więc narazie przyjmiemy sobie pewne sałe

# oznaczenia:
g = 9.81         # można zmienic jak coś narazie jako stała w [m/s^2]
h = 1.0          # wysokość z jakie rozpoczynamy rzut [m]
Vo = 20         # prędkość początkowa [m/s]
alfa = 60      # kąt nachylenia wektora Vo od poziomu w stopniach ustalić przdział
x = 0.0          # odległość od początku rzuty
y = 0.0          # wysokość od cała od pionu
t = 0.0          #calkowity czas lotu
H = 0.0          #maksymalna wysokosc ns jaka wzniesie sie cialo od wysokosci poczatkowej
Hmax = 0.0          #maksymalna wysokosc na jaka wzniesie sie cialo
z = 0.0         #zasieg rzutu

def PrędkośćPoczątkowych(alfa,Vo):                    #progra liczący skłodwe prędkość początkowych
    if alfa >= 0 and alfa <= 90 or alfa >= 270 and alfa <=360:
        sinalf = np.around(np.sin(np.deg2rad(alfa)),4)
        cosalf = np.around(np.cos(np.deg2rad(alfa)),4)
        Vox = np.around(Vo * cosalf,4)
        Voy = np.around(Vo * sinalf,4)
        print('składowa prędkość początkowej wzdłuż x:', Vox\
              , 'składowa prędkość początkowej wzdłuż y:', Voy)
        return ([Vox, Voy])
    elif alfa > 90 and alfa < 270:
        print('rzucasz za siebie nie zbyt mądrze, odwróć się i zrób to jak należy')
        return [0,0]
    else:
        print('trzymaj się przedziału!')
        return [0,0]

def CzasLotu(Voy,g, wybor):                                #program liczacy calkowity czas lotu
    # y = h + Voy*t - 1/2*g*t^2  oraz y = tg(beta)*t
    #po kilku przekształceniach otrzymamy h + t*(Voy - tg(beta)) - 1/2*g*t^2 = 0
    # znajdujemy pierwiastki funkcji kwadratowej
    a = -g/2
    b = Voy - np.tan(np.deg2rad(beta))
    c = h
    delta = (b*b) - 4*a*c
    t1 = (-b - math.sqrt(delta)) / (2*a)
    t2 = (-b + math.sqrt(delta)) / (2*a)
    if t1 >= t2:
        t = np.around(t1,4)
    else:
        t = np.around(t2,4)
    print('Czas lotu wynosi t =', t)
    return (t)

def MaxWysokosc(Voy,g):                                #program liczacy maksymalna wysokosc ciała
    H = np.around((Voy ** 2) / (2 * g), 4)
    Hmax = H + h
    print('maksymalna wysokosc na jaka wzleci cialo to H =',Hmax,'m')
    return (Hmax)

def Zasieg(Vox,t):
    z = np.around(Vox * t, 4)
    print('Zasieg rzutu to z =', z,'m')
    return (z)

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
m = float(input('Masa ciała ma wynosić m = '))


Vox,Voy = PrędkośćPoczątkowych(alfa,Vo)
t = CzasLotu(Voy,g,wybor)
Hmax = MaxWysokosc(Voy,g)
z = Zasieg(Vox,t)
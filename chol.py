import numpy as np
import math
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def Diff(sol, t):
    k = 1500
    k21 = 1.0
    k12 = 3.58
    mtis = 0.234
    mout = 1.2
    Mout = 6.05
    m_in = 0.8
    Min = 1.9
    r1 = 90
    r2 = 120
    r3 = 420
    r4 = 555
    w1 = 0.1496
    w2 = 0.0233
    dm1dt = k / sol[0] + k21 * sol[1] - k12 * sol[0] - mout - (1 - Heaviside(r1, t / 60)) * Mout * (
        math.sin(w1 * t / 60)) ** 2 + m_in + Heaviside(r2, t / 60) * (
                    1 - Heaviside(r3, t / 60)) * Min * (math.sin(w1 * (t / 60 - r2)) ** 2)
    dm2dt = -k21 * sol[1] + k12 * sol[0] - mtis + Heaviside(r3, t / 60) * (
            1 - Heaviside(r4, t / 60)) * Mdiet * (math.sin(w2 * (t / 60 - r3)) ** 2)

    return [dm1dt, dm2dt]


def Heaviside(r, tm):
    if (tm < r):
        return 0
    else:
        return 1

def Viewgraph():
    t = np.linspace(0, 200000)
    y0 = [2400, 8600]
    sol = odeint(Diff, y0, t)
    plt.plot(t / 60, sol[:, 0], 'r--', linewidth=2.0, label="Cholesterol in liver")
    plt.plot(t / 60, sol[:, 1], 'b--', linewidth=2.0, label="Cholesterol in blood")
    plt.xlabel("time(min)")
    plt.ylabel("Amount of cholesterol")
    plt.legend()
    plt.grid()
    plt.show()

def main():
    while True:
        print("1) change value\n2) show model\n3) information\n0) exit")
        ch = input()
        if ch == '1':
            print("insert number: ")
            md = float(input())
            if md >= 0:
                global Mdiet
                Mdiet = md
                Viewgraph()
            else:
                print("Wrong value\n")
        if ch == '2':
            Mdiet = 2
            Viewgraph()
        if ch == '0':
            return
        if ch == '3':
            print("Программа разработана для наглядной демонстрации гомеостаза холестерина в теле человека.\n"
                  "По умолчанию приняты среднестатистические показатели.\n"
                  "При изменении коэффициента можно посмотреть гомеостаз при повышенном(коэффициент больше 3)\n"
                  "и пониженном (коэффициент меньше 2) потреблении холестерина. Стандартное значение 2.\n")

main()

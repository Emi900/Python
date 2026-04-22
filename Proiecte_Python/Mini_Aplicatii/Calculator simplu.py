# Calculator simplu in Python 

operatii = input("Introdu urmatoarele operatii (+ - * /): ")
n1 = float(input("Introdu 1 numar: "))
n2 = float(input("Introdu al-2-lea numar: "))

if operatii == "+":
    rezultat = n1 + n2
    print(round(rezultat, 2))
elif operatii == "-":
    rezultat = n1 - n2
    print(round(rezultat, 2))
elif operatii == "*":
    rezultat = n1 * n2
    print(round(rezultat, 2))
elif operatii == "/":
    rezultat = n1 / n2
    print(round(rezultat, 2))
else:
    print("NU ai introdus + - * /")
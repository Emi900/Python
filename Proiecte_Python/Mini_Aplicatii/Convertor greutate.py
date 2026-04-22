# Convertor de greutate 

greutate = float(input("Introdu greutatea: "))
unit = input("(Kg sau L): ")

if unit == "Kg":
    greutate = greutate * 2.205
    unit = "L"
    print(f"Greutatea ta este: {round(greutate, 1)} {unit}")
elif unit == "L":
    greutate = greutate / 2.205
    unit = "Kg"
    print(f"Greutatea ta este: {round(greutate, 1)} {unit}")
else: 
    print(f"{unit} nu este valida")


# if = Do some code only IF some condition is True
#      Else do somthing else 


age = int(input("Introdu varsta: "))

if age >= 100:
    print("esti pre batran ")    
elif age >= 18:
    print("Te-ai inregistrat cu succes!")
elif age < 0:
    print("NU esti nascut ")
else:
    print("Nu te poti inregistra!!!")
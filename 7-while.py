# The Complete Python Course For Beginners - @credits Tech With Tim
# Beginner Python Programming
#
# While Loops

pasword = ""

while True:
    pasword = input("Escribe una contraseña: ")
    if len(pasword) < 8:
        print("La contraseña debe tener al menos 8 caracteres")
    else:
        print("Cantidad de caracteres correctos")
        break

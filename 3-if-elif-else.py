# The Complete Python Course For Beginners - @credits Tech With Tim
# Beginner Python Programming
#
# If-Elif-Else

age = input ( 'Ingresa tu edad: ')

if int(age) == 16:
    print(f'Tienes 16 años')
elif int(age) > 16:
    print(f'Tienes más de 16 años')
else:
    print(f'Tienes menos de 16 años')

print (f"Tienes {age} años") if int(age) == 16 else print ("No tienes 16 años")
# The Complete Python Course For Beginners - @credits Tech With Tim
# Beginner Python Programming
#
# String Methods

# .strip()  quita los espacios en blanco
# .len()    nos da el largo de la cadena
# .lower()  pasa la cadena a minúsculas
# .upper()  pasa la cadena a mayúsculas
# .split()  CREA UNA LISTA DE UNA CADENA A PARTIR DEL DELIMITADOR QUE PONGAMOS. Si no ponemos nada separa por un espacio.

cadena = input('Escribe una cadena de texto: ')
separador = input('Cuál separador te gustaría usar? ')

print(cadena.split(separador)) if separador != "" else print(cadena.split(' '))

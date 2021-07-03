# The Complete Python Course For Beginners - @credits Tech With Tim
# Beginner Python Programming
#
# Iteration by items

fruits = ['apples', 'pears', 'strawberrys']

for fruit in fruits:  # Iteration by item
    if fruit == 'pears':
        print(fruit)
    else:
        print('not pears')

for x in range(len(fruits)):  # Iteration by index
    if fruits[x] == 'pears':
        print(fruits[x])
    else:
        print('not pears')

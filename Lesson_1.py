print("************************************* Здравствуй пользователь! ************************************* ")
print("                         ____________________________________________________")

fruits = ['Яблоко', 'Груша', 'Банан', 'Апельсин']
print(fruits)
print()

fruits.append('Мандарин')
print('_______________ После добавления _________________')
print(fruits)
print()

for fruit_num, fruit in enumerate(fruits, start=1):
    print(fruit_num, fruit)
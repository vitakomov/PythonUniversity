name = input("Enter your name: ")
immutable_var = (5,6,7,5.6,"aaa",name)
#name = input("Enter your name again: ")           Провел эксперимент, так значение не меняется
#immutable_var[0] = 7            Не работает, неизменяемый список. PyCharm предлагает tuple в list перевести
#immutable_var[6] = input("Enter your name again: ")         Так тоже
print(immutable_var)


mutable_list = [1.4,7,8,"bbb",name]
mutable_list[0] = "ccc"
#name = input("Enter your name again: ")         Тут тоже значение не меняется
num = mutable_list.index(name) if name in mutable_list else -2
if num!=-2: mutable_list[num] = input("Enter your name again: ")   #Так меняется, но переменная перезаписывается строкой
print(mutable_list)



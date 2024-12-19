my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
num = 0
while num < len(my_list):
    if my_list[num] < 0:
        break
    elif my_list[num] == 0:
        continue
    else:
        print(my_list[num])
    num += 1
#Понимаю, что по условиям задачи требуется while и continue, сделал решение с ними
#Но для вариант без continue и с циклом for из следующего урока мне кажется более правильный
print("__________________")
for i in my_list:
    if i < 0:
        break
    elif i > 0:
        print(i)

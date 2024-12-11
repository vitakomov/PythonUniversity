from datetime import datetime

my_string = input("Enter anything pls: ")
sting_length = len(my_string)
print("String length: ", sting_length)
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(" ",""))
print(my_string[0])
print(my_string[-1])

#Очень уж захотелось переделать программу для определения возраста из урока, приложу ее ниже
#Хотелось бы совета, как еще можно улучшить, спасибо! :)

current_year = datetime.now().year
current_month = datetime.now().month
print("Now is: ",datetime.today().year,"y-",datetime.today().month,"m-",datetime.today().day,"d",sep="")
year_of_birth = input("Enter your year of birth: ")
while not year_of_birth.isdigit():
    year_of_birth = input("Enter year of birth in digits, please! ")
if int(year_of_birth)>=current_year: print("Welcome, man from future!")
else:
    month_of_birth = input("Enter your month of birth: ")
    while not (month_of_birth.isdigit() and 1 <= int(month_of_birth) <= 12):
        month_of_birth = input("Enter your month of birth from 1 (january) to 12 (december): ")
    if int(month_of_birth)<=current_month: print("You are ", current_year - int(year_of_birth))
    else: print("You are ", current_year - int(year_of_birth)-1)




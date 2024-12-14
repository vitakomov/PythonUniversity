def is_float_check(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


#Словари
my_dict = {"Dima":2000,"Dasha":2002,"Petya":1999}
print("Dictionary: ",my_dict)
print("Dasha's year: ",my_dict["Dasha"])
my_dict["Olya"] = 2003
name_ = input("Enter your name: ")
year_ = input("Enter your year of birth: ")
while not year_.isdigit: year_ = input("Enter your YEAR of birth in digits: ")
year_ = int(year_)
my_dict[name_] = year_
print("Deleting Petya:",my_dict.pop("Petya"))
print("Edited dictionary:", my_dict)

#Множества
my_set = {1,2,3,3,5,1,0.5,6,0.5,"aaa","aaa"}
print("Set: ",my_set)
my_set.add("bbb")
my_set.add("ccc")
discard_ = input("Enter data to delete: ")
if discard_.isdigit(): discard_ = int(discard_)
elif is_float_check(discard_): discard_ = float(discard_)
if discard_ in my_set: my_set.remove(discard_)
else: print("Data not in set")
print("Modified set: ",my_set)






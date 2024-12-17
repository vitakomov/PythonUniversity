def input_number(count_):
    input_str = str("Enter a number " + str(count_) + ": ")
    number_ = input(input_str)
    while not number_.isdigit(): number_ = input("Wrong input, please try again: ")
    return number_

print("Enter 3 numbers")
first = input_number(1)
second = input_number(2)
third = input_number(3)
match_ = 0
if first == second and first == third: match_ = 3
elif first == second or first == third or second == third: match_ = 2
print(match_)

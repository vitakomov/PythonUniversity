from fake_math import divide as divfake
from true_math import divide as divtrue

result1 = divfake(69, 3)
result2 = divfake(3, 0)
result3 = divtrue(49, 7)
result4 = divtrue(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)

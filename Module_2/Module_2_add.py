n = input("Enter a number from 3 to 20: ")
try :
    n = int(n)
except :
    print("Invalid input")
    quit()
if n < 3 or n > 20:
    print("Wrong number")
    quit()
result = ""
for i in range(1, n):
    for j in range(i+1, n):
        if n % (i+j) == 0:
            result = result + str(i) + str(j)
print (result)

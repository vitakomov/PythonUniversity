def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(2, 4)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [1, True, "ssss"]
values_dict = {"a": 3, "b": False, "c": "aaaaa"}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, "String"]
print_params(*values_list_2, 42)
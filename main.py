
def print_params(a = 1, b = 'строка', c = True):
    print(f"a = {a}, b = {b}, c = {c}")


print_params()
print_params(2)
print_params(2, 'new string')
print_params(2, 'new string', False)
print_params(b = 25)
print_params(c = [1, 2, 3])
values_list = [10, 'new string', False]
values_dict = {'a': 11, 'b': '2_string', 'c': 65}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
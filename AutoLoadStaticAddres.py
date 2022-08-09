import os
os.system("cls")

B_R = '{' 
B_L = '}'

address_file_user = input("***All your static addresses must be from 'assets' file***\nenter address target file: ")

with open(r"{}".format(address_file_user), encoding="utf8") as file:
    string = file.read()

string_to_list_split = string.split('"')
string_to_list_split.append('"=<!-- assets/ -->"')

n = 1
while '"=<!-- assets/ -->"' not in string_to_list_split[n]:
    string_to_list_split[n] = f"'{string_to_list_split[n]}'"
    print(f'done {n}')
    n += 2


run = 0
for i in string_to_list_split:

    if 'assets/' in i:
        address_in_tag = f'"{B_R}% static {i} %{B_L}"'
        i_index = string_to_list_split.index(i)
        string_to_list_split[i_index] = address_in_tag
        print("static done")
        result = ''

        if run == 0 and i == '"=<!-- assets/ -->"':
            string_to_list_split.pop()
            result = result.join(string_to_list_split)
            back_dir = (os.path.dirname(f'{address_file_user}'))
            address_new_file = back_dir + "\RESULT.html"

            with open(r"{}".format(address_new_file), "a" ,encoding='utf-8') as f:
                f.write('{% load static %}\n' + result)
            print('*************************************The Code Changed*************************************')
            print('The modified code named "RESULT.html" was built next to the input file at this address.')
            print(address_new_file)
            finish = input('Press a key finished :')
            run += 1
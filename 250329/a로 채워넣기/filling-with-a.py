string = input()
string = list(string)

string[1] = 'a'
string[len(string)-2] = 'a'

new_string = "".join(string)
print(new_string)
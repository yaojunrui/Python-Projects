"""

string1 = "WorD"
string2 = "owrd"
print(string1)
string1 = string1.lower()
string1 = sorted(string1)
string2 = string2.lower()
string2 = sorted(string2)
print(string1)
print(string2)
if string1 == string2:
    print("True")

string_list = list(string1)
print(string_list)

"""

numlist = [23, 332, 13, 32, 3, 12]
print(numlist[1:])
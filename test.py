string1 = 'Damage85 (Sword)'
string2 = 'erherh83werewr'

# Using filter, isdigit, and int to extract numbers
number2 = int(''.join(filter(str.isdigit, string2)))

print(''.join(filter(str.isdigit, string1)))





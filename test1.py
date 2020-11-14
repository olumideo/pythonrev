first_num = 2
second_num = 8
new_rate = first_num ** second_num
print(str(new_rate) + ' is the new rate!')

## input always take in string by default. Use DATA-TYPE CONVERSION
new_first_num = input("What is x? ")
new_second_num = input("What is the tax value? ")
# print(new_first_num * new_second_num) ## *** This throws up an
# exception because you cannot multiple two strings together. Use TYPE 
# conversion
# print(int(new_first_num) * int(new_second_num))


'''
print('Hello in a revision')
first_name = input("What is your first name?")
last_name = input("What is your last name?")
'''

#print(first_name + last_name)
'''
print("Hello "+ first_name.capitalize() + " " + last_name.capitalize())
print("Yhello, {1} {0}".format(first_name, last_name.upper()))
print(f'You are welcome {first_name} {last_name}')
'''


'''
reword = "Dette er en ny setninger!"
print(reword.upper())
print(reword.capitalize())
print(reword.count('e'))
'''
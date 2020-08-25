# WHILE LOOPS EXERCISES

# Enter a random string in the variable string_1, then enter a character and save it in the variable char_1.
# Write code, which will count how many times your character is included in your string.
# Save result to result_1 variable

string_1 = "Krasnodar russian Federation"
char_1 = "r"
result_1 = 0
index = 0
while index < len(string_1):
    if string_1[index] == char_1:
        result_1 += 1
    index += 1
print(result_1)


# Enter a random number and save it in variable number_1. Then create code to multiply all the digits together
# and save result in the result_2 variable.

number_1 = 123
string_number = str(number_1)
counter = 0
result_2 = 1
while counter != len(string_number):
    result_2 *= int(string_number[counter])
    counter += 1
print(result_2)


# Enter a random number and save it in variable number_2. Then create code which will return
# a number with digits of number_1 in reverse order. Save it in result_3 variable

number_2 = 157
# string_number_2 = str(number_2) # convert number to string
# result_3 = int(string_number_2[::-1]) # revers string and convert back to number
string_number_2 = str(number_2)
counter = len(string_number_2)
string_result = ""
while counter > 0:
    string_result += string_number_2[counter-1]
    counter -= 1
result_3 = int(string_result)
print(result_3)
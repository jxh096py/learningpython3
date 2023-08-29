def addition(a, b):
    return int(a) + int(b)

number_a = input()
number_b = input()

print("the first number you've entered is:" + number_a)
print("the second number you've entered is:" + number_b)


# // WRONG - the print function interprets '+' characters are concatenations
# print(number_a + "+" + number_b + "=" + number_a+number_b) 

# we have to convert the String format of the numbers to integers to perform mathematical operations
sum = int(number_a) + int(number_b)

# We have to convert the variable 'sum' back to string so we can print it out in the print() function
print(number_a + "+" + number_b + "=" + str(addition(number_a, number_b))) 



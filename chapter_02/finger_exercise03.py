num_x = int(input("How many times should I print the letter X? "))
to_print = ""
num = 0

while num < abs(num_x):
    num +=1
    to_print += "x"

print(to_print)
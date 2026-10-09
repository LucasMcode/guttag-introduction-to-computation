x = int(input("Insert a number for x: "))
y = int(input("Insert a number for y: "))
z = int(input("Insert a number for z: "))

num_list = [x, y, z]
odd_numbers = []

for num in num_list:
    new_number = num
    if new_number % 2 != 0:
        odd_numbers.append(new_number)
if odd_numbers:
    print(max(odd_numbers))
else:
    print(min(num_list))
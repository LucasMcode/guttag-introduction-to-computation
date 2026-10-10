num = 0
largest_odd = None
while num < 10:
    new_number = int(input("Give a number: "))
    if new_number %2 != 0:
        if  largest_odd == None or new_number > largest_odd:
            largest_odd = new_number
    num +=1
if largest_odd is None:
    print("No odd number!")
else:
    print(largest_odd)
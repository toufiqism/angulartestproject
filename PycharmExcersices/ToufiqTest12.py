start = int(input("Enter first = "))

end = int(input("Enter second = "))

choice = int(input("Press 1 to print odd numbers or 2 to print even numbers ="))
sum = 0
if start > end:
    step = -1
else:
    step = 1

for i in range(start, end + 1, step):

    if choice == 1:
        if i % 2 != 0:
            print(i, end=" ")
            sum = sum + i

    else:
        if i % 2 == 0:
            print(i, end=" ")
            sum = sum + i
print()
print('Total is = ', sum)

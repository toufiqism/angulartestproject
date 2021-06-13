start = int(input("Enter first = "))

end = int(input("Enter second = "))

choice = int(input("Press 1 to print odd numbers or 2 to print even numbers ="))
sum = 0
avg = 0
n = 0
if start > end:
    step = -1
    end = end - 1
else:
    step = 1
    end = end + 1

for i in range(start, end, step):
    if choice == 1:
        if i % 2 != 0:
            print(i, end=" ")
            sum = sum + i
            n = n + 1
            avg = sum / n

    else:
        if i % 2 == 0:
            print(i, end=" ")
            sum = sum + i
            n = n + 1
            avg = sum / n

print()
print('Total is = ', sum)
print()
print('Avg is = ', avg)

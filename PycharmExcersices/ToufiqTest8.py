# def eggs(someParameter):
#     someParameter.append('Hello')
#
#
# spam = [1, 2, 3]
# eggs(spam)
# print(spam)
import copy

spam = [1, 2, 1]

temp = spam.copy()

spam[1] = 'Cheese'

print(temp)
print(spam)

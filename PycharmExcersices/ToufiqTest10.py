spam = ['apples', 'bananas', 'tofu', 'cats']


def separate(any_value):
    for i in range(len(any_value)):
        print(any_value[i])


separate(spam)

picnicItems = {'apples': 5, 'cups': 2}

print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')

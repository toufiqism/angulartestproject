def collatz_sequence(number):
    while number > 0:
        if number % 2 == 0:
            number = number / 2
            print('Collatz Number -> ', number)
        elif number % 2 != 0:
            odd_collatz_number = 3 * number + 1
            print('Collatz Number -> ', odd_collatz_number)
            number = odd_collatz_number
        if number == 1:
            break


collatz_sequence(int(input('Enter Number for collatz sequencing: ')))

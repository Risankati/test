# -*- coding: utf-8 -*-
# And now for something completely different

number = 88

print('Živ! Ugan številko, če lahko!')
print ('Hint: ni 42')
print ('Life hint: Never trust a computer you can\'t throw out the window')

while True:
    guess = int(raw_input("Guess:"))
    if guess < number:
        print('Prenizko, sucka')

    if guess > number:
            print('Did you smoke smth, cus you high')

    if guess == number:
        print('GG')
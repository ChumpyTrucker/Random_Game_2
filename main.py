from random import randint

import sys

answer = randint(int(sys.argv[2]), int(sys.argv[3]))

while True:
    try:
        guess = int(input(f'guess a number {sys.argv[2]}~{sys.argv[3]}:  '))
        if  0 < guess < 11:
            if guess == answer:
                print('You are the best!!!')
                break
        else:
            print('hey bozo, I said 1~10')
    except ValueError:
        print('please enter a number')
        continue

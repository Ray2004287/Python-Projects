import random
secret_number = random.randint(1,10)
max_treis = 5
tries = 0

print('Welcomt to number guessing game ')
print("i'm thinking of number between 1 and 100")
print(f'you have {max_treis}tries')

while tries < max_treis:
    guess = int(input(f'Try {tries + 1} : '))
    tries += 1

    if guess < secret_number:
        print('Too low')
    elif guess > secret_number:
        print('Too high')
    else:
        print(f'correct is in {tries} tries ')
        break
else:
    print(f'is done ! the correct number is {secret_number}')
import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    attempts = 0

    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 10. Попробуйте его угадать.")

    while True:
        try:
            user_guess = int(input("Введите ваше предположение: "))
            attempts += 1
        except ValueError:
            print("Пожалуйста, введите целое число.")
            continue

        if user_guess < number_to_guess:
            print("Загаданное число больше.")
        elif user_guess > number_to_guess:
            print("Загаданное число меньше.")
        else:
            print(f"Поздравляю! Вы угадали число за {attempts} попыток.")
            break

guess_the_number()

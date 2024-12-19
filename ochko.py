import random

cards = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4

random.shuffle(cards)

points = 0

def show_status(points, cards_left):
    print(f"Ваши очки: {points}")
    print(f"Осталось карт: {cards_left}")

while True:
    show_status(points, len(cards))

    choice = input("Будете брать карту? (y/n): ").strip().lower()

    if choice == 'n':
        print(f"Вы завершили игру с {points} очками.")
        break
    elif choice == 'y':
        if not cards:
            print("Карты закончились!")
            break

        card = cards.pop()
        points += card

        if points > 21:
            print(f"Вы проиграли! Ваши очки: {points}")
            break
        elif points == 21:
            print(f"Поздравляем! Вы выиграли с {points} очками!")
            break
    else:
        print("Неверный ввод. Пожалуйста, введите 'y' или 'n'.")

print("Спасибо за игру!")

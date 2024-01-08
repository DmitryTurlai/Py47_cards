import os, curses
from random import randint

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Cards:

    def __init__(self):
        pass

    def visual(self, mast, number, x, y):

        if number == 11:
            number = "B"
        elif number == 12:
            number = "Д"
        elif number == 13:
            number = "K"
        elif number == 14:
            number = "Т"

        if mast == 1:
            return (f'''
         ________________
        | {number}            {number} |
        |                |
        |     __  __     |
        |    (  \\/  )    |
        |     \\    /     |
        |      \\  /      |
        |       \\/       |
        |                |
        |                |
        | {number}            {number} |
        |________________|
        ''')
        elif mast == 2:
            return (f'''
         ________________
        | {number}            {number} |
        |                |
        |       /\\       |
        |      /  \\      |
        |     /    \\     |
        |     \\    /     |
        |      \\  /      |
        |       \\/       |
        |                |
        | {number}            {number} |
        |________________|
        ''')
        elif mast == 3:
            return (f'''
         ________________
        | {number}            {number} |
        |       /\\       |
        |     /####\\     |
        |   /#########\\  |
        | (############) |
        |   \\########/   |
        |      |##|      |
        |     |####|     |
        | {number}            {number} |
        |________________|
        ''')

        elif mast == 4:
            return (f'''
         ________________
        | {number}            {number} |
        |                |
        |      ####      |
        |      ####      |
        | ############## |
        | ############## |
        |      ####      |
        |      ####      |
        |                |
        | {number}            {number} |
        |________________|
        ''')
    def choice_card(self, unique_card):
        while True:
            ms = randint(1, 4)
            nm = randint(2, 14)
            pair = ms, nm

            if pair in unique_card:
                continue
            else:
                unique_card.add(pair)
                break

        return ms, nm

    def count(self, nm):
        sum = 0
        if nm == 11:
            sum = 2
        elif nm == 12:
            sum = 3
        elif nm == 13:
            sum = 4
        elif nm == 14:
            sum = 1
        else:
            sum = nm
        return sum

sum_t = 0
unique_card = set()
cards = Cards()

ms, nm = cards.choice_card(unique_card)
sum_t = cards.count(nm)
print(cards.visual(ms, nm, 20, 12))

ms, nm = cards.choice_card(unique_card)
sum_t += cards.count(nm)
print(cards.visual(ms, nm, 20, 12))

print(f"Сумма очков Ваших карта = {sum_t}")

while True:
    if int(input("Если хотите еще одну карту - введите 1, если хватит - введите 0")) == 1:
        ms, nm = cards.choice_card(unique_card)
        sum_t += cards.count(nm)
        print(cards.visual(ms, nm, 20, 12))
        print(f"Сумма очков Ваших карта = {sum_t}")
        if sum_t > 21:
            print("ПЕРЕБОР, ВЫ ПРОИГРАЛИ")
            break
        elif sum_t == 21:
            print("ИДЕАЛЬНО! ВЫ ПОБЕДИЛИ!")
            break
    else:
        print(f"Сумма очков Ваших карта = {sum_t}")
        comp = randint(2, 26)
        if comp > 21:
            print(f"ВЫ ВЫИГРАЛИ. У МЕНЯ ПЕРЕБОР. Сумма очков = {comp}")
        elif comp > sum_t:
            print(f"ВЫ ПРОИГРАЛИ. У меня сумма очков = {comp}")
        elif comp < sum_t:
            print(f"ВЫ ВЫИГРАЛИ!!! У меня сумма очков = {comp}")
        elif comp == sum_t:
            print(f"НИЧЬЯ!!! У меня сумма очков = {comp}")
        break


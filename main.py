#import os
#import time
#import random

#statystyki
wins = 0
losses = 0

decks_amount = input("How many decks do you want to play?")

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * (4 * int(decks_amount))

def card_deck(n = 8): # zrobione przez Joltimas DZIAŁA
    #print('random_card')
    card_value = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    card_type = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    list = []

    for z in range(n):
        for x in card_value:
            elemtennt = []
            for y in card_type:
                elemtennt = [x, y]
                list.append(elemtennt)
    print(list)
    return list

def random_card(card_value,car_type): #funkcja która losuje kartę
    print('random_card')

def hit(): #dobieranie karty
    print('hit')

def sum_of_cards(): #liczy sumę kart
    print('sum_of_cards')

def stats(): #oczywiste
    print('stats')

def rules(): #oczywiste
    print('rules')

def iq_krupier(): #poziom zawansowania krupiera (słabiak, dobry krupier, midas)
    print('iq_krupier')


def play_again(): #oczywiste
    again = input("Do you want to play again? ( Y / N )")
    if again == "Y":
        dealer_hand = []
        player_hand = []
        game()
    else:
        print("Bye! Bay!")
        exit()
    print('play_again')

def game(): #tutaj dzieje się gra, połączyć z mainem
    print('game')


def main():#tutaj dać przywitanie i wszytkie inne pierdoły, wybór opcji, statystyka
    print('mian')
    game()


if __name__ == '__main__':
    print('Black Jack!!!')
    main()

#import os
#import time
#import random

#statystyki
wins = 0
losses = 0

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * (4 * int(decks_amount))
decks = 1


def card_deck(n): #zrobione przez Joltimas DZIAŁA  
    g=n
    card_value = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    card_type = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    number_of_decks = 1
    number_of_midas = 4
    list=[]
    for z in range (g):
        for x in card_value:
            elemtennt=[]
            for y in card_type:
                elemtennt=[x, y]
                list.append(elemtennt)

    return list

def random_card(deck): #zrobione przez Joltimas DZIAŁA funkcja która losuje kartę,zajebista 
    print(len(deck))
    a=(random.randint(0, len(deck)))
    b=deck[a]
    #print(b)
    return b
    
def hit(deck, stol): #zrobione przez Joltimas DZIAŁA dobieranie karty i wyświetlanie jej 

    b=random_card(deck)
    print(b)
    stol.append(b)
    for x in stol: 
        for y in x: 
            print(y,end=" ")
        print(" ")
    print(stol)


def game(): #zrobione przez Joltimas DZIAŁA tutaj dzieje się gra,połączyć z mainem

    print("\n\t\tWELCOME TO BLACKJACK!\n")
    decks = input("Enter number of decks to use:\t")

    deck=card_deck(1)
    #print(deck)
    #print(len(deck))
    #print(a)
    #b=random_card(a)
    #print(b)
    #print('Black Jack!!!')
    stol=[]
    #print(hit(deck, stol))
    hit(deck, stol)

def sum_of_cards(): #liczy sumę kart
    pass


def stats(): #oczywiste
    pass

def rules(): #oczywiste
    pass


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
        game()

    else:
        print("Bye!")
        exit()


def main():
    game()


if __name__ == "__main__":
    main()

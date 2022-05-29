import random
import os
import time



import random
import os
import time
def card_deck(n): #zrobione przez Joltimas DZIAŁA  
    g=n
    card_value = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    card_type = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
<<<<<<< HEAD
    number_of_decks = 1;
    number_of_midas = 4
    #proba
=======
    list=[]
    for z in range (g):
        for x in card_value:
            elemtennt=[]
            for y in card_type:
                elemtennt=[x,y]
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
def main():
    game()
if __name__ == "__main__":
    main()

def sum_of_cards(): #liczy sumę kart

def stats(): #oczywiste

def rules(): #oczywiste
>>>>>>> 253392f14661de28e84b6e7e97354d0e47f226a9


def iq_krupier(): #poziom zawansowania krupiera(słabiak, dobry krupier, midas)

def play_again(): #oczywiste

def game(): #tutaj dzieje się gra,połączyć z mainem

def print_hi(name):
    print(name) 


def print_hi():#tutaj dać przywitanie i wszytkie inne pierdoły, wybór opcji, statystyka
    game()



if __name__ == '__main__':
    print_hi('Black Jack!!!')

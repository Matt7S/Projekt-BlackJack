import random
import os
import time



def card_deck(n=8): # zrobione przez Joltimas DZIAŁA  
    
    card_value = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    card_type = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    list=[]
    for z in range (n):
        for x in card_value:
            elemtennt=[]
            for y in card_type:
                elemtennt=[x,y]
                list.append(elemtennt)
    print(list)
    return list

def random_card(card_value,car_type): #funkcja która losuje kartę,zajebista

def hit(): #dobieranie karty

def sum_of_cards(): #liczy sumę kart

def stats(): #oczywiste

def rules(): #oczywiste


def iq_krupier(): #poziom zawansowania krupiera(słabiak, dobry krupier, midas)

def play_again(): #oczywiste

def game(): #tutaj dzieje się gra,połączyć z mainem

def print_hi(name):
    print(name)


def main():#tutaj dać przywitanie i wszytkie inne pierdoły, wybór opcji, statystyka
    game()



if __name__ == '__main__':
    print_hi('Black Jack!!!')

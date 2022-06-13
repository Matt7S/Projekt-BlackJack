#!/usr/bin/python
# -*- coding: utf-8 -*-

#import os
import random
#import time

decks = input("Wybierz liczbe  talii: \n")

#uzycie chcianej liczby talii
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * ( int(decks) * 4)

#inicjalizacja wygranych oraz przegranych podczas jednego ciagu gier
wins = 0
losses = 0

# przywitanie sie z graczem
def hello():
    print("\n\t\t\t    Witaj w Blackjack!\n")
    menu=input(print("[G]ra,[S]tatystyki,[Z]asady,[R]anga \n"))
    if menu == "g":
        tryb=input(print("Wybierz tryb gry: [c]zas/[b]ez czasu"))
        #if tryb== "c":
            #tryb gry na czas
        if tryb== "b":
            game()
        else:
            hello()
    elif menu == "s":
        print("\tWYGRANE: " + str(wins) + "\tPRZEGRANE: " + str(losses) + "\n")
        back=input("Kliknij q, aby wrócić do menu")
        if back == "q":
            hello()
    elif menu == "z":
        print("https://pl.wikipedia.org/wiki/Blackjack")
        back=input("Kliknij q, aby wrócić do menu")
        if back == "q":
            hello()
    elif menu == "r":
        rank()
        back=input("Kliknij q, aby wrócić do menu")
        if back == "q":
            hello()
    else:
        hello()
def rank():
    percentage=wins/(wins+losses)*100
    if percentage<20:
        print("Brąz")
    elif 20<=percentage<40:
        print("Srebro")
    elif 40<=percentage<60:
        print("Złoto")
    elif 60<=percentage<80:
        print("Platyna")
    elif 80<=percentage<100:
        print("Diament")
    elif percentage==100:
        print("Mistrz")

#funkcja ktora przypisuje dwie poczatkowe karty
def deal(deck, number):
    hand = []
    for i in range(number):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"
        hand.append(card)
    return hand




#funkcja ktora sumuje wartosc danego posiadacza kart
def total(hand):
    total = 0
    #J, Q i K maja wartosc rowna 10
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total += 10
            #wartosc asa jest zalezna od tego ile wart jest deck
        elif card == "A":
            total=total+11
            if total>21:
                total=total-10
        # jesli zadn6e z powyzszych to po prostu dodawana jest wartosc karty
        else: total += card
    return total

# dodanie jednej kolejnej karty podczas HIT
def hit(hand):
    card = deck.pop()
    if card == 11:card = "J"
    if card == 12:card = "Q"
    if card == 13:card = "K"
    if card == 14:card = "A"
    hand.append(card)
    return hand


def back(hand):
    back=input(print("Czy chciałbyś cofnąć ruch? [t]/[n]"))
    if back == "t":
        del hand[-1]
    return hand

#funkcja wypisujaca statystyki, bez wyniku rezultatu
def print_results(dealer_hand, player_hand):


    #print("\tWINS: " + str(wins) + "\tLosses: " + str(losses)+ "\n")
    print("\n")
    print("Dealer punkty:\t" +  str(total(dealer_hand)) + "\t i posiada karty:\t" + str(dealer_hand))
    print("Twoje punkty:\t" +   str(total(player_hand)) + "\t i posiada karty:\t" + str(player_hand))


#funkcja wypisujaca na samym koncu szczegoly koncowego wyniku gry
def score(dealer_hand, player_hand):
    global wins
    global losses

    #najpierw sprawdzany jest warunek czy gracz nie ma równo 21 punktów
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("Gratulacje! Masz Blackjacka!\n")
        wins += 1

    #nastepnnie sprawdzany jest warunek czy dealer ma 21 pkt
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("Niestety, dealer ma blackjacka. Przegrales.\n")
        losses += 1

    #nastepnie sprawdzane jest czy gracz nie ma wiecej niz 21 punktow
    elif total(player_hand) > 21:
        print_results(dealer_hand, player_hand)
        print ("Niestety, masz wiecej niz 21 punktow. Przegrales.\n")
        losses += 1

    #sprawdzenie czy dealer ma wiecej niz 21 punktow
    elif total(dealer_hand) > 21:
        print_results(dealer_hand, player_hand)
        print ("Dealer ma wiecej niz 21 punktow. Wygrales!\n")
        wins += 1

    #sprawdzenie czy gracz ma mniej punktow niz dealer
    elif total(player_hand) < total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print ("Niestety. Twoj wynik jest nizszy nie dealera. Przegrales.\n")
        losses += 1

    #sprawdzenie czy gracz ma wiecej punktow niz dealer
    elif total(player_hand) > total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print ("Gratulaccje. Masz wyzszy wynik niz dealer. Wygrales!\n")
        wins += 1

    elif total(player_hand)==total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print ("REMIS.\n")

def game():
    global wins
    global losses
    choice = 0




    dealer_hand = deal(deck, 2)
    player_hand = deal(deck, 2)

    print("Dealer pokazuje " + str(dealer_hand[0]))

    print("Masz nastepujace karty " + str(player_hand) + " o liczbie punktow: " + str(total(player_hand)) +"\n")

    if total(player_hand) == 21:
        score(dealer_hand, player_hand)
        wins += 1
        back_to_menu()

    quit = False

    while not quit:
        choice = input("Do wyboru: [H]it, [S]tand, or [Q]uit: \n").lower()
        if choice == 'h':
            hit(player_hand)
            print("Twoje karty: " + str(player_hand))
            print("Twoje punkty: " + str(total(player_hand)) + "\n")
            back(player_hand)
            if total(player_hand) > 21:
                if "A" in player_hand:
                    sum=total(player_hand)-10
                    if sum>21:
                        score(dealer_hand,player_hand)
                        losses+=1
                        back_to_menu()
                    else:
                        score(dealer_hand,player_hand)
                        wins+=1
                        back_to_menu()
                else:
                    losses += 1
                    score(dealer_hand, player_hand)
                    back_to_menu()

            elif total(player_hand) == 21:
                score(dealer_hand, player_hand)
                wins += 1
                back_to_menu()

        elif choice == 's':
            while total(dealer_hand) < 17:
                print("Dealer dobiera karte")
                hit(dealer_hand)
                if total(dealer_hand) > 21:
                    wins += 1
                    score(dealer_hand, player_hand)
                    back_to_menu()
            score(dealer_hand, player_hand)
            back_to_menu()
        elif choice == "q":
            print("Do zobaczenia!")
            exit()
def back_to_menu():
    back=input(print("Czy chcesz wrócić do menu [t]/[n]\n")).lower()
    if back == "t":
        hello()
    else:
        game()

def main():
    hello()
    game()
    back_to_menu()

if __name__ == "__main__":
   main()
#Kieren Singh Gill
#11/10/2020
#Python Fall 2020, Section 1
#GillKieren_Assign8_extra_credit.py

#import random module
import random
import sys

#cards list
cards  = ['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts', '6 of Hearts', '5 of Hearts', '4 of Hearts', '3 of Hearts', '2 of Hearts', 'Ace of Hearts', 'King of Hearts', 'Queen of Hearts', 'Jack of Hearts', '10 of Diamonds', '9 of Diamonds', '8 of Diamonds', '7 of Diamonds', '6 of Diamonds', '5 of Diamonds', '4 of Diamonds', '3 of Diamonds', '2 of Diamonds', 'Ace of Diamonds', 'King of Diamonds', 'Queen of Diamonds', 'Jack of Diamonds', '10 of Clubs', '9 of Clubs', '8 of Clubs', '7 of Clubs', '6 of Clubs', '5 of Clubs', '4 of Clubs', '3 of Clubs', '2 of Clubs', 'Ace of Clubs', 'King of Clubs', 'Queen of Clubs', 'Jack of Clubs', '10 of Spades', '9 of Spades', '8 of Spades', '7 of Spades', '6 of Spades', '5 of Spades', '4 of Spades', '3 of Spades', '2 of Spades', 'Ace of Spades', 'King of Spades', 'Queen of Spades', 'Jack of Spades']
#values list
values = [10, 9, 8, 7, 6, 5, 4, 3, 2, [1,11], 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, [1,11], 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, [1,11], 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, [1,11], 10, 10, 10]

#choose a random card from cards list
#store it in card1 and card2
card1 = random.choice(cards)
card2 = random.choice(cards)

#obtain the corresponding values
#store them in value1 and value2
value1 = values[cards.index(card1)]
value2 = values[cards.index(card2)]

#player's current hand
player_hand_cards = [card1, card2]

#compute possible sums of player's current hand
#if one of the values is a list value, it means it one of the cards is an Ace
#compute the possible sums depending on how many Aces are in hand


#if there are 2 Aces
if (type(value1) == list) and (type(value2) == list):
    sum1 = value1[0] + value2[0]
    sum2 = value1[1] + value2[0]
    player_hand_total = [sum1,sum2]
#if the first card is an ace
elif (type(value1) == list):
    sum1 = value1[0] + value2
    sum2 = value1[1] + value2
    player_hand_total = [sum1,sum2]
#if the second card is an ace
elif (type(value2) == list):
    sum1 = value2[0] + value1
    sum2 = value2[1] + value1
    player_hand_total = [sum1,sum2]
#if there are no aces
else:
    sum1 = value1 + value2
    player_hand_total = [sum1]

#remove cards from deck
#remove corresponding values
del values[cards.index(card1)]
del values[cards.index(card2)]
cards.remove(card1)
cards.remove(card2)


print("================================ RESTART ================================")
print()
#let player know their cards and hand value
if len(player_hand_total) == 2:
    print("Player hand:",player_hand_cards, "is worth", player_hand_total[0], "or", player_hand_total[1])
elif len(player_hand_total) == 1:
    print("Player hand:", player_hand_cards, "is worth", player_hand_total[0])
print()
#if the player gets a blackjack they win
#program ends
if 21 in player_hand_total:
    print("Player wins!")
    sys.exit()
    
#ask user if they would like to hit or stand
choice = input("(h)it or (s)tand? ")
#data validation to make sure user can only progress if they enter 'h' or 's'
    #create a while loop
    #if user input is not 'h' or 's', reprompt them
while choice not in ['h','s']:
    print("Invalid option!")
    choice = input("(h)it or (s)tand? ")
    
#if the user chooses to hit
if choice == 'h':
    card3 = random.choice(cards)
    value3 = values[cards.index(card3)]
    del values[cards.index(card3)]
    cards.remove(card3)
    player_hand_cards = [card1, card2, card3]
    #if user draws an ace
    if (type(value3) == list):
        #if user has any more aces, this ace must be worth 1 so user doesn't bust
        if (type(value1)==list) or (type(value2)==list):
            value3 == 1
            #add 1 to all values in the list
            player_hand_total = [i + value3 for i in player_hand_total]
            #if any values are above 21, remove from list
            for i in player_hand_total:
                if i > 21:
                    player_hand_total.remove(i)
        #if the user doesn't have any more aces        
        else:
            player_hand_total = [i + 11 for i in player_hand_total]
            for i in range(len(player_hand_total)):
                if player_hand_total[i] > 21:
                    player_hand_total[i] = player_hand_total[i] - 10
            print("Player hand:",player_hand_cards, "is worth", player_hand_total[0], "or", player_hand_total[1])

    
         
    if 21 in player_hand_total:
        print("Player wins!")
        sys.exit()
        

#unfinished***

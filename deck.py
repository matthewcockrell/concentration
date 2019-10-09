#Matthew Cockrell
#deck.py
#Implementation of a Deck of Cards - Designed for use in a Pygame application


import pygame
from random import randint

class Deck:
    cards = [] #The list of cards
    size = 52  #The size of the deck will always be 52, as we are accouting for 4 suites, each with 13 cards

    #Initialze a new deck of cards 
    def __init__(self):
        self.cards.append(Card("hearts", "ace")) #Initialize the hearts 
        for num in range(2, 11):
            self.cards.append(Card("hearts", str(num)))
        self.cards.append(Card("hearts", "jack"))
        self.cards.append(Card("hearts", "queen"))
        self.cards.append(Card("hearts", "king"))

        self.cards.append(Card("clubs", "ace")) #Initialize the clubs
        for num in range(2, 11):
            self.cards.append(Card("clubs", str(num)))
        self.cards.append(Card("clubs", "jack"))
        self.cards.append(Card("clubs", "queen"))
        self.cards.append(Card("clubs", "king"))

        self.cards.append(Card("spades", "ace")) #Intitialize the spades 
        for num in range(2, 11):
            self.cards.append(Card("spades", str(num))) 
        self.cards.append(Card("spades", "jack"))
        self.cards.append(Card("spades", "queen"))
        self.cards.append(Card("spades", "king"))

        self.cards.append(Card("diamonds", "ace")) #Initialize the diamonds 
        for num in range(2, 11):
            self.cards.append(Card("diamonds", str(num)))
        self.cards.append(Card("diamonds", "jack"))
        self.cards.append(Card("diamonds", "queen"))
        self.cards.append(Card("diamonds", "king"))

        #Set the corresponding image and color for each card 
        for card in self.cards:
            image = pygame.image.load("PlayingCards/PNG-cards-1.3/"+card.toString()+".png")
            back_image = pygame.image.load("PlayingCards/PNG-cards-1.3/back.png")
            card.image = pygame.transform.scale(image, (100,125)) #Scale the image correctly
            card.back_image = pygame.transform.scale(back_image, (100, 125))
            if card.suite == "hearts" or card.suite == "diamonds":
                card.color = "red"
            elif card.suite == "spades" or card.suite == "clubs":
                card.color = "black"
            

    #Shuffle the deck of the cards 
    def shuffle(self):
        for card in self.cards:
            card.deck_pos = randint(0, 1000)
        self.sort()

    #Implementation of bubble sort to sort the cards based on deck position number
    def sort(self):
        deck_of_cards = self.cards
        bubble = 0
        while bubble < len(deck_of_cards):
            for i in range (0, len(deck_of_cards)-1):
                if deck_of_cards[i].deck_pos >= deck_of_cards[i+1].deck_pos: #Compare each pair of cards 
                    temp = deck_of_cards[i+1]
                    deck_of_cards[i+1] = deck_of_cards[i]
                    deck_of_cards[i] = temp #Swap if the 1st card has a position number greater than the 2nd
            bubble += 1
        self.cards = deck_of_cards


    #Return a string representation of the deck
    def toString(self):
        deckStr = ""
        for card in self.cards:
            deckStr += card.toString() + "\n"
        return deckStr

#Card class to represent a card
class Card:
    def __init__(self, suite, number):
       se lf.suite = suite
        self.number = number
        self.color = "No Color Assigned"
        self.deck_pos = 0
        self.image = None
        self.back_image = None
        self.screen_pos_top = 0
        self.screen_pos_left= 0
        
    
    #Return a string representation of the card 
    def toString(self):
        return (self.number + "_of_" + self.suite)
    




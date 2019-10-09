#Matthew Cockrell
#card_game.py
#Implementation of the "Concentration" memory card-game using Pygame 

import pygame 
from deck import Deck, Card

#Begin by showing the instructions on the screen until the user clicks the screen
def show_instructions(screen): 
    instructions = pygame.image.load("instructions.png")
    pygame.transform.scale(instructions, (1500, 1050))
    screen.blit(instructions, (0,0))
    pygame.display.flip()
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                break
                
            if event.type == pygame.MOUSEBUTTONDOWN: #Begin the game when the user clicks
                loop = False
                break


def main():
    pygame.init()
    pygame.display.set_caption("Memory Game - Concentration")
    screen = pygame.display.set_mode((1500,1050))  

    show_instructions(screen) #Show the instructions 

    screen.fill((76, 171, 3))
    running = True #Set the main game loop to true 

    deck = Deck()
    deck.shuffle() #Create and shuffle the deck of cards 

    #Set up the board by displaying all of the face-down cards
    left = 25
    top = 100
    count = 0
    for j in range(0, 5): #5 rows 
        for i in range (count, count+10): #10 cards in each row 
            left += 125
            deck.cards[i].screen_pos_left = left #Keep track of the left, or X, position of the card 
            deck.cards[i].screen_pos_top = top #Keep track of the top, or Y, position of the card 
            surface = deck.cards[i].back_image.convert()
            screen.blit(surface, (deck.cards[i].screen_pos_left, deck.cards[i].screen_pos_top))
        count = count + 10
        top = top + 150
        left = 25

    #The two additional cards go on the sixth row 
    deck.cards[50].screen_pos_left = 150
    deck.cards[50].screen_pos_top = 850
    surface = deck.cards[50].back_image.convert()
    screen.blit(surface, (deck.cards[50].screen_pos_left, deck.cards[50].screen_pos_top))

    deck.cards[51].screen_pos_left = 275
    deck.cards[51].screen_pos_top = 850
    surface = deck.cards[51].back_image.convert()
    screen.blit(surface, (deck.cards[51].screen_pos_left, deck.cards[51].screen_pos_top))
       
    pygame.display.flip() #Write changes to the screen 
    
    count_cards_selected = 0 #Keep track of the number of cards selected per turn 
    player_turn = 0 #Even = player one's turn, odd = player two's turn 
    player_one_score = 0 #Keep track of the scores for each player 
    player_two_score = 0
    
    black = (0, 0, 0)
    font = pygame.font.Font('freesansbold.ttf', 32) 
    one_text = font.render("Player One Score: " + str(player_one_score), True, black) #Display each players's score
    screen.blit(one_text, (550, 910))
    two_text = font.render("Player Two Score: " + str(player_two_score), True, black)
    screen.blit(two_text, (1050, 910))

    player_one_text = font.render("Player One's Turn!", True, (255,255,255)) #Display the current player's turn
    player_two_text = font.render("Player Two's Turn!", True, (255,255,255))
    screen.blit(player_one_text, (800, 1000))
   
    pygame.display.flip()


    #Main game loop 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN: #Player clicks a card 
                x, y = event.pos #pinpoint the coordinates of the click
                for card in deck.cards:
                    if card.image.get_rect(left=card.screen_pos_left, top=card.screen_pos_top).collidepoint(x,y): #Did they click a card?
                        if count_cards_selected == 0: #Make sure they can't click the same card twice
                            last_card_selected = card.toString()
                        if count_cards_selected == 1:
                            if card.toString() == last_card_selected: #If clicking the same card twice, break the loop
                                break
                        count_cards_selected+=1 #Update the number of cards selected 
                        screen.blit(card.image.convert(), (card.screen_pos_left, card.screen_pos_top)) #turn over the card 
                        pygame.display.flip()
                        if count_cards_selected == 1: #Output helpful messages to the console - not seen in the GUI
                            selected_card_one = card
                            print("Card One: " + selected_card_one.toString() + " (" + selected_card_one.color + ")")
                        elif count_cards_selected == 2:
                            selected_card_two = card
                            print("Card Two: " + selected_card_two.toString() + " (" + selected_card_two.color + ")")
        
        #Check for a match if the player has selected two cards 
        if count_cards_selected == 2:
            #We have a match! 
            if selected_card_one.color == selected_card_two.color and selected_card_one.number == selected_card_two.number: #Color and number (rank) must match
                print("It's a match!")
                count_cards_selected = 0
                if player_turn % 2 == 0: #Is this player one's turn? 
                    screen.fill((76, 171, 3), one_text.get_rect(left=550, top=910))
                    screen.fill((76, 171, 3), player_one_text.get_rect(left=800, top=1000))
                    player_one_score += 1
                    player_turn += 1
                    one_text = font.render("Player One Score: " + str(player_one_score), True, black) 
                    print("Player One's Score is now: ", player_one_score)
                    screen.blit(one_text, (550, 910)) #Display player one's new score
                    screen.blit(player_two_text, (800, 1000)) #Change the current player text to player 2
                    pygame.display.flip()
                    

                elif player_turn % 2 == 1: #Is this player two's turn? 
                    screen.fill((76, 171, 3), two_text.get_rect(left=1050, top=910))
                    screen.fill((76, 171, 3), player_two_text.get_rect(left=800, top=1000))
                    player_two_score += 1
                    player_turn+=1
                    print("Player Two's Score is now: ", player_two_score)
                    two_text = font.render("Player Two Score: " + str(player_two_score), True, black)
                    screen.blit(two_text, (1050, 910)) #Display player two's new score
                    screen.blit(player_one_text, (800, 1000)) #Change the current player text to player 1
                    pygame.display.flip()
            else:
                print("No Match!")
                count_cards_selected = 0
                start_timer = pygame.time.get_ticks()
                time_counting = True
                while time_counting:
                    seconds = (pygame.time.get_ticks()-start_timer)/1000
                    if seconds > 1.5:
                        screen.blit(selected_card_one.back_image.convert(), (selected_card_one.screen_pos_left, selected_card_one.screen_pos_top))
                        screen.blit(selected_card_two.back_image.convert(), (selected_card_two.screen_pos_left, selected_card_two.screen_pos_top))
                        if player_turn % 2 == 0:
                            screen.fill((76, 171, 3), player_one_text.get_rect(left=800, top=1000))
                            screen.blit(player_two_text, (800, 1000))
                            pygame.display.flip()
                            player_turn += 1
                        elif player_turn % 2 == 1:
                            screen.fill((76, 171, 3), player_two_text.get_rect(left=800, top=1000))
                            screen.blit(player_one_text, (800, 1000))
                            pygame.display.flip()
                            player_turn += 1
                        break
                        
if __name__ == "__main__":
    main()
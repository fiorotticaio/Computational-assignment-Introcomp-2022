import pygame
import sys
from window import Window


if __name__ == "__main__":
  pygame.init() # Initialize pygame

  game_window = Window(1024, 768) # Create a window object
  screen = pygame.display.set_mode((game_window.get_width(), game_window.get_height())) # create game screen
  pygame.display.set_caption("RPG do Cainho e do Trabinha") # Set the window title
  screen.fill(game_window.get_color()) # Fill the screen with the window color
  clock = pygame.time.Clock() # Create a clock object


  #================= Menu scene =================== (TODO: colocar dentro de uma função / modularizar)
  background_image = pygame.image.load('assets/background.png')
  background_rect = background_image.get_rect() # Get the rectangle of the background image
  background_rect.center = (game_window.get_width() // 2, game_window.get_height() // 2) # Center the background image

  pygame.display.set_caption('Choose your character') # Set the window title

  font = pygame.font.Font(None, 50) # Create a font object
  title = font.render('Choose your character', True, (255, 255, 255))
  title_rect = title.get_rect() # Get the rectangle of the title
  title_rect.center = (game_window.get_width() // 2, 50) # Center the title

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit() # Quit the game

    screen.blit(background_image, background_rect) # Draw the background image
    screen.blit(title, title_rect) # Draw the title

    # Draw the characters
    # for personagem in personagens:
    #     screen.blit(personagem['imagem'], personagem['posicao'])

    pygame.display.flip() # Update the screen
    clock.tick(60) # Limit the FPS to 60
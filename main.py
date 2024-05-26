import pygame

# Main function defined
def main():

    # Initialize pygame module
    pygame.init()

    # Set screen with size 240x180
    screen = pygame.display.set_mode((240,180))
    
    # Variable that controls the main loop
    running = True

    # Main loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()

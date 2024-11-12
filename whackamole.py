import pygame



def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:

        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()

        #pygame.draw.line(screen, (0,0,0), (x1, y1), (x2, y2))

        width = 20
        height = 16
        square_size = 32

        screen.blit(mole_image, mole_image.get_rect(topleft=(1, 2)))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

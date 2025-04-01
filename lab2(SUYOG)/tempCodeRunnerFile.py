import pygame

def main():
    pygame.init()
    
    # Set up display
    gd = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Polygon Animation")
    
    poly = [(250, 200), (200, 300), (300, 300), (250, 200)]
    fill_color = (255, 0, 0)
    background_color = (255, 255, 255)
    
    # Draw initial polygon
    gd.fill(background_color)
    pygame.draw.polygon(gd, fill_color, poly)
    pygame.display.flip()
    pygame.time.delay(1000)
    
    # Animate the polygon
    for _ in range(50):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        poly[0] = (poly[0][0] - 1, poly[0][1])
        poly[3] = (poly[3][0] + 1, poly[3][1])
        
        gd.fill(background_color)
        pygame.draw.polygon(gd, fill_color, poly)
        pygame.display.flip()
        pygame.time.delay(100)

    # Draw the circles
    for c in range(1, 26):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        pygame.draw.circle(gd, (0, 255, 0), (250, 250), 75 - c)
        pygame.display.flip()
        pygame.time.delay(9)

    pygame.time.delay(1000)
    pygame.quit()

if __name__ == "__main__":
    main()

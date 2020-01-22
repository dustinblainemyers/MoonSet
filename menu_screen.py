# Menu Screen

def show_menu_screen():
    screen.blit(intro_background, intro_background_rect)
    # draw_text(screen, "THIS IS THE MENU SCREEN", 64, WIDTH / 2, HEIGHT / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # Any key press will start the game
            if event.type == pygame.KEYDOWN:
                waiting = False


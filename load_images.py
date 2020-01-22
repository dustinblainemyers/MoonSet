# Load all game graphics
background = pygame.image.load(path.join(img_dir, "6776.jpg")).convert()
background_rect = background.get_rect()
intro_background = pygame.image.load(
    path.join(img_dir, 'Intro.png')).convert()
intro_background_rect = intro_background.get_rect()
congratulations_image = pygame.image.load(
    path.join(img_dir, "congratulations.png"))
congratulations_image_rect = congratulations_image.get_rect()
game_over_image = pygame.image.load(path.join(img_dir, "game_over.png"))
game_over_image_rect = game_over_image.get_rect()
player_img = pygame.image.load(path.join(img_dir, "playerShip.png")).convert()
player2_img = pygame.image.load(
    path.join(img_dir, "player2Ship.png")).convert()
boss_moon = pygame.image.load(path.join(img_dir, "moon.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "laserRed01.png")).convert()
enemy_bullet_img = pygame.image.load(
    path.join(img_dir, "laserGreen02.png")).convert()
enemy_images = []
enemy_list = ['enemyBlack2.png', 'enemyBlue3.png',
              'enemyGreen4.png', 'enemyRed5.png']
for img in enemy_list:
    enemy_images.append(pygame.image.load(
        path.join(enemy_ship_dir, img)).convert())
import pygame
from random import randint as rn

pygame.init()
WIDTH, HEIGHT = 800, 600
gWindow = pygame.display.set_mode((WIDTH, HEIGHT))  # Game window
pygame.display.set_caption("Taffy The Bird")
BG = pygame.image.load("Assets/BG/TaffyTheBirdBG.png")  # Picture of Taffy the Bird
imageTaffy = pygame.transform.scale(pygame.image.load("Assets/Taffy.png"), (100, 100))
groundPart = pygame.image.load("Assets/BG/GroundPartOfBG.png")  # Game background image
sizeDifferenceForTaffy = 120  # Size difference between obstacles for Taffy to be able to fit in
obFirst1 = pygame.transform.scale(pygame.image.load("Assets/Obstacle/Obstacle(top).png"), (70, 500))
obFirst2 = pygame.transform.scale(pygame.image.load("Assets/Obstacle/Obstacle(bottom).png"), (70, 500))
obSecond1 = pygame.transform.scale(pygame.image.load("Assets/Obstacle/Obstacle(top).png"), (70, 500))
obSecond2 = pygame.transform.scale(pygame.image.load("Assets/Obstacle/Obstacle(bottom).png"), (70, 500))
obThird1 = pygame.transform.scale(pygame.image.load("Assets/Obstacle/Obstacle(top).png"), (70, 500))
obThird2 = pygame.transform.scale(pygame.image.load("Assets/Obstacle/Obstacle(bottom).png"), (70, 500))
startScreen = pygame.image.load("Assets/StartScreen.png")
font = pygame.font.Font("Assets/Fonts/Roboto/static/RobotoMono-BoldItalic.ttf", 40)
gameOverFont = pygame.font.Font("Assets/Fonts/Roboto/static/RobotoMono-BoldItalic.ttf", 60)
arrOfHeights = [
    [-250, 370], [-200, 420], [-300, 320], [-180, 440],
    [-240, 380], [-400, 220], [-320, 300], [-160, 460],
    [-230, 390], [-140, 480], [-370, 250], [-285, 335],
    [-260, 360], [-280, 340], [-190, 430], [-330, 290]
]
pygame.display.update()


def move(ob1, ob2, ob3, ob4, ob5, ob6):
    ob1.x -= 2
    ob2.x -= 2
    ob3.x -= 2
    ob4.x -= 2
    ob5.x -= 2
    ob6.x -= 2


def TaffyCanJump(bird, key):
    if key[pygame.K_SPACE]:
        if bird.y < -25:
            bird.y = -26
        else:
            bird.y -= 8
    else:
        if bird.y > HEIGHT - 161:
            bird.y = HEIGHT - 160
        else:

            bird.y += 3
    pygame.display.update()


def taffyAction(bird, obst1, obst2, obst3, obst4, obst5, obst6):
    randIndex1 = rn(0, len(arrOfHeights) - 1)
    randIndex2 = rn(0, len(arrOfHeights) - 1)
    randIndex3 = rn(0, len(arrOfHeights) - 1)

    # background
    gWindow.blit(BG, (0, 0))
    # Taffy
    gWindow.blit(imageTaffy, (bird.x, bird.y))

    # obstacles
    gWindow.blit(obFirst1, (obst1.x, obst1.y))
    gWindow.blit(obFirst2, (obst2.x, obst2.y))
    gWindow.blit(obSecond1, (obst3.x, obst3.y))
    gWindow.blit(obSecond2, (obst4.x, obst4.y))
    gWindow.blit(obThird1, (obst5.x, obst5.y))
    gWindow.blit(obThird2, (obst6.x, obst6.y))

    if obst1.x < -100:
        obst1.x, obst2.x = WIDTH + 200, WIDTH + 200
        obst1.y, obst2.y = arrOfHeights[randIndex1][0], arrOfHeights[randIndex1][1]
    if obst3.x < -100:
        obst3.x, obst4.x = WIDTH + 200, WIDTH + 200
        obst3.y, obst4.y = arrOfHeights[randIndex2][0], arrOfHeights[randIndex2][1]
    if obst5.x < -100:
        obst5.x, obst6.x = WIDTH + 200, WIDTH + 200
        obst5.y, obst6.y = arrOfHeights[randIndex3][0], arrOfHeights[randIndex3][1]

    move(obst1, obst2, obst3, obst4, obst5, obst6)

    if bird.colliderect(obst1) or bird.colliderect(obst2) or bird.colliderect(obst3) or bird.colliderect(obst4) or \
            bird.colliderect(obst5) or \
            bird.colliderect(obst6):
        return True


def TaffyTheBird():
    runIt = True
    startTheGame = False
    clock = pygame.time.Clock()
    Taffy = pygame.Rect((WIDTH // 2 - 200, HEIGHT // 2), (70, 50))
    FPS = 60
    score = 0
    randIndex1 = rn(0, len(arrOfHeights) - 1)
    randIndex2 = rn(0, len(arrOfHeights) - 1)
    randIndex3 = rn(0, len(arrOfHeights) - 1)
    obst1 = pygame.Rect((WIDTH // 2 + 400, arrOfHeights[randIndex1][0]), (70, 460))
    obst2 = pygame.Rect((WIDTH // 2 + 400, arrOfHeights[randIndex1][1]), (70, 470))
    obst3 = pygame.Rect((WIDTH // 2 + 800, arrOfHeights[randIndex2][0]), (70, 460))
    obst4 = pygame.Rect((WIDTH // 2 + 800, arrOfHeights[randIndex2][1]), (70, 470))
    obst5 = pygame.Rect((WIDTH // 2 + 1200, arrOfHeights[randIndex3][0]), (70, 460))
    obst6 = pygame.Rect((WIDTH // 2 + 1200, arrOfHeights[randIndex3][1]), (70, 470))
    weStop = False
    while runIt:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runIt = False
        if not startTheGame:
            gWindow.blit(startScreen, (0, 0))
            pressedS = pygame.key.get_pressed()
            if pressedS[pygame.K_s]:
                startTheGame = True
        else:
            if not weStop:
                pressedKey = pygame.key.get_pressed()
                TaffyCanJump(Taffy, pressedKey)
                scoreTextRect = pygame.Rect((10, 540), (10, 40))
                if taffyAction(Taffy, obst1, obst2, obst3, obst4, obst5, obst6):
                    weStop = True
                    scoreTextRect.x = - 400
                # ground
                scoreText = font.render(f"Score: {score}", False, (120, 150, 40))

                gWindow.blit(groundPart, (0, 513))
                gWindow.blit(scoreText, (scoreTextRect.x, scoreTextRect.y))
                pygame.display.update()
                if Taffy.x == obst1.x + 10 or Taffy.x == obst3.x + 10 or Taffy.x == obst5.x + 10:
                    score += 1
                    gWindow.blit(scoreText, (10, 540))
                    pygame.display.update()
            else:
                gameOver = gameOverFont.render("Game Over", False, (255, 255, 0))
                gameScore = gameOverFont.render(f"Score: {score}", False, (255, 255, 20))
                dataBaseFile = open("Assets/ScoreFile", "r")
                bestScore = dataBaseFile.readlines()[0]
                dataBaseFile.close()
                if score > int(bestScore):
                    bestScore = score
                    dataBaseFile = open("Assets/ScoreFile", "w")
                    dataBaseFile.write(str(score))
                    dataBaseFile.close()
                bestScoreDisplay = gameOverFont.render(f"Best: {bestScore}", False, (255, 255, 20))
                pressR = font.render("Press R to restart", False, (225, 255, 0))
                gWindow.blit(gameOver, (WIDTH // 2 - 150, HEIGHT // 2 - 100))
                gWindow.blit(gameScore, (WIDTH // 2 - 140, HEIGHT // 2 - 40))
                gWindow.blit(bestScoreDisplay, (WIDTH // 2 - 140, HEIGHT // 2 + 20))
                gWindow.blit(pressR, (WIDTH // 2 - 200, HEIGHT // 2 + 90))
                pressedR = pygame.key.get_pressed()
                if pressedR[pygame.K_r]:
                    TaffyTheBird()
                    break

        pygame.display.update()


if __name__ == "__main__":
    TaffyTheBird()

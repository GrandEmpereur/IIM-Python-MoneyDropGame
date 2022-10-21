import pygame as pg
import os
from assets.question import *
from assets.checkAnwsers import *
from assets.textWraper import *
from assets.nextQuestion import *
import time

pg.init()
pg.font.init()
pg.mixer.init()

screen = pg.display.set_mode((1136, 640))
pg.display.set_caption("My Game")

# Game Loop
running = True
i = 0
category = Questions.get_category(Questions)

while running:
    # MUSIC BACKGROUND
    pg.mixer.music.load(os.path.join("src/assets", "sounds", "music.mp3"))
    pg.mixer.music.play(-1)
    pg.mixer.music.set_volume(0.5)

    # BACKGROUND IMAGE
    background = pg.image.load("images/Money-Drop.png")
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    i = i+1

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                # run the check answer function
                correct = checkButton(
                    button, button2, button3, button4, answers, correct_answer)

    # CATEGORY
    for i in range(len(category)):
        font = pg.font.Font(None, 30)
        text = category[0]
        text_surface = font.render(text, True, (0, 0, 0))
        screen.blit(text_surface, (300, 80))

    # QUESTION
    question = Questions.get_question(Questions, category[0])
    # wrap text to fit the screen width
    question = wrap_text(question, pg.font.Font(None, 30), 500)
    # draw the text to the screen
    for i in range(len(question)):
        font = pg.font.Font(None, 30)
        text = question[i]
        text_surface = font.render(text, True, (0, 0, 0))
        screen.blit(text_surface, (300, 120 + i * 30))

    # ANSWERS
    answers = Questions.get_answers(Questions, category[0])
    i = 0
    for answer in answers:
        text_surface = font.render(answer, True, (0, 0, 0))
        screen.blit(text_surface, (200 + 200*i, 320))
        i = i+1

    # BUTTONS ANSWERS
    button = pg.Rect(190, 439, 150, 90)
    button2 = pg.Rect(390, 439, 150, 90)
    button3 = pg.Rect(590, 439, 150, 90)
    button4 = pg.Rect(790, 439, 150, 90)

    pg.draw.rect(screen, (0, 0, 0), button, 1)
    pg.draw.rect(screen, (0, 0, 0), button2, 1)
    pg.draw.rect(screen, (0, 0, 0), button3, 1)
    pg.draw.rect(screen, (0, 0, 0), button4, 1)

    # CHECK ANSWER
    correct_answer = Questions.get_correct_answer(Questions, category[0])
    checked = checkButton(button, button2, button3,button4, answers, correct_answer)

    # NEXT QUESTION
    if checked == True:
        category = Questions.get_category(Questions)
        question = Questions.get_question(Questions, category[0])
        answers = Questions.get_answers(Questions, category[0])
        correct_answer = Questions.get_correct_answer(Questions, category[0])
        i = 0
        for answer in answers:
            text_surface = font.render(answer, True, (0, 0, 0))
            screen.blit(text_surface, (200 + 200*i, 320))
            i = i+1

    # END GAME
    # if i == 5:
    #     running = False
    # if checked == False:
    #     running = False

    pg.display.flip()
pg.quit()

# CHECK ANSWERs
import pygame as pg
from assets.question import *

pg.init()
pg.font.init()
pg.mixer.init()
screen = pg.display.set_mode((1136, 640))

def checkAnswer(answers, correctAnswers):
    if answers == correctAnswers:
        correct = True
    else:
        correct = False
    return correct

def changeBackground(correct, button):
    if correct:
        pg.draw.rect(screen, (0, 255, 0), button)
    else:
        pg.draw.rect(screen, (255, 0, 0), button)

def checkButton(button, button2, button3, button4, answers, correctAnswers):
    if button.collidepoint(pg.mouse.get_pos()):
        if pg.mouse.get_pressed()[0]:
            correct = checkAnswer(answers[0], correctAnswers)
            changeBackground(correct, button)
            return correct

    if button2.collidepoint(pg.mouse.get_pos()):
        if pg.mouse.get_pressed()[0]:
            correct = checkAnswer(answers[1], correctAnswers)
            changeBackground(correct, button2)
            return correct

    if button3.collidepoint(pg.mouse.get_pos()):
        if pg.mouse.get_pressed()[0]:
            correct = checkAnswer(answers[2], correctAnswers)
            changeBackground(correct, button3)
            return correct

    if button4.collidepoint(pg.mouse.get_pos()):
        if pg.mouse.get_pressed()[0]:
            correct = checkAnswer(answers[3], correctAnswers)
            changeBackground(correct, button4)
            return correct
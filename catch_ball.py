﻿import pygame
from ball import Ball
from setting import Settings
from unit import Unit
from setting import Setting


def catch_ball(): #Что это? У Шара нет такого класса? Почему у тебя функция вне класса. Свечников же нас за такое повесит! Х((
    set=Setting()
    ball = Ball(screen=screen, sets=sets)
    unit= Unit(screen=screen, sets=sets)

    while True:
        if set.finish == False :
            ball.drop_ball(sets=sets)    
            f.update_ball(ball=ball, bowl=bowl, sets=sets)






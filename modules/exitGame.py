#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
+ FileName  =  exitGame.py
+  Created  =  30/07/2005
+   Author  =  DecosSoft
+  Version  =  1.0
"""

from modules import efects, styles
from modules.language import language
from os import system
from time import sleep

admin=styles.Admin

def exitGame(lang, prompt, retries=3):
    negativa=['n','no']
    positive=['y','yes'] 
    positiva=['s','si']                 
    while True:
        ok= input(prompt)
        respuesta=ok.lower()
        if respuesta in negativa:
            system('clear')
            print()
            efects.Writer(admin.Plus+language(lang)(17),3)       
            print('\n')
            exit()
        elif respuesta in positive or respuesta in positiva:
            #system('clear')
            print()
            efects.Writer(admin.Plus+language(lang)(18),3)
            sleep(1)
            system('clear')
            return True
        else:
            retries-=1
            if retries<0:
                print()
                efects.Writer(admin.Minus+language(lang)(19),3)
                print('\n')
                exit()
            print()
            print(admin.Warning+language(lang)(16))
            




#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
+ FileName  =  hangman.py
+  Created  =  30/07/2005
+   Author  =  DecosSoft
+  Version  =  1.0
"""

from modules import styles, efects
from os import system

color=styles.Ascii
banner=color.green+'''=============='''+color.end+''' Lenguaje: Python 3 '''+color.green+'''===========================
'''+color.end+'''============== Hecho por: DecosSoft ========================
'''+color.red+'''=============='''+color.end+''' La informacion te hara libre '''+color.red+'''==============='''+color.end

message=color.yellow+'''
" Este sencillo programa fue hecho con fines educativos y 
sin finalidad de lucro. Puedes usarlo modificarlo, compartirlo 
cuando quieras, solo recuerda respetar los créditos "
'''+color.end

efects.Writer(banner,1)
efects.Writer(message,4)
print('\n')

def begining():
    print(styles.Admin.Run+' inicializando', end=' ')
    efects.Writer('[................]',25)
    system('clear')


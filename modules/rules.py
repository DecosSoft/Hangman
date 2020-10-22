#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
+ FileName  =  rules.py
+  Created  =  30/07/2005
+   Author  =  DecosSoft
+  Version  =  1.0
"""

from modules import styles

rules=styles.Ascii.grey+'''
 [+] Encuentra la palabra secreta, ingresando una
     letra a la vez, dentro de 6 intentos.
 [+] Para salir durante el juego, escribe la palabra "exit".
 [+] Para adivinar la palabra secreta, ingresa "guess". 
     Si te equivocas, pierdes el juego.
'''+styles.Ascii.end

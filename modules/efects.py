#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
+ FileName  =  efects.py
+  Created  =  30/07/2005
+   Author  =  DecosSoft
+  Version  =  1.0
"""

from sys import stdout
from time import sleep

def Writer(string,z):
    sleep(0.3)
    for i in string + '\n':
        stdout.write(i)
        stdout.flush()
        sleep(z / 100)


    

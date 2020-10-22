from modules import efects, tries, styles
from modules.language import language
from time import sleep
from os import system
from sys import exit

color=styles.Ascii
admin=styles.Admin

def userWin(lang, word, prompt):
    if prompt==word:
        system('clear')
        print(color.green+language(lang)(7)+color.white)
        efects.Writer(tries.images.get(7),1)
        print(color.green+language(lang)(8),color.yellow+word)
        efects.Writer(color.red+language(lang)(9),8)
        return True
    else:
        return False

def userWin_or_Lose(lang, prompt, word):
    if prompt=='exit':
        print()
        exit()
    elif prompt=='guess':
        print()
        print(admin.Run+language(lang)(10), end=' ')           
        solution=input(''+color.green)
        if solution==word:
            return word
        else:
            return 'userLoss'
    else:
        return
                    
def userInput(lang, prompt, inputs, word):
    while True:
        answer=' '   
        prompt=prompt.lower()
        if prompt=='exit' or prompt=='guess':
            incognito=userWin_or_Lose(lang, prompt,word)
            return incognito       
        if prompt in answer or prompt in inputs or len(prompt)>1:
            if prompt in inputs:
                print()
                print(admin.Warning+language(lang)(11))
                print()
                prompt=input(admin.Run+language(lang)(12)+color.green)
            else:
                print()
                print(admin.Warning+language(lang)(13))
                print()
                prompt=input(admin.Run+language(lang)(12)+color.green)
        else:            
            return prompt
       
def userLoss(lang, word):
    system("clear")
    print(color.red+language(lang)(14)+color.white)
    efects.Writer(tries.images.get(6),1)
    print(color.red+language(lang)(15),color.yellow+word)
    efects.Writer(color.red+language(lang)(9),8)
    return False
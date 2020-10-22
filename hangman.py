from modules import logo, styles, tries, validate,efects, exitGame, rules
from random import choice
from os import system
from time import sleep
from modules.banner import begining
from modules.language import language

admin=styles.Admin
color= styles.Ascii

def randomWord():
    f=open('words.txt','r')
    rand=choice(f.readlines())
    word,clue=rand.split(':')[0], rand.split(':')[1]
    f.close()
    return word, clue
    
def maskWord(word):
    mask=[]
    [mask.append('__') for x in word if x!=' ']
    [mask.insert(x,' ') for x in range(len(word)) if word[x]==' ']
    return mask
    
def showImage(lang, clue, trie, mask, inputs): 
    print('\n\t {0} '.format(clue))
    print(tries.images.get(trie))
    joinMask=' '.join(mask)
    print(color.yellow+'\n    ',joinMask)
    inputs="".join(inputs)
    if ' ' in mask:
        x=len(mask)-1
    else:
        x=len(mask)
    print('\n')
    print(admin.Info+ language(lang)(0),color.yellow+str(x))
    print(admin.Info+language(lang)(1),color.red+str(6-trie))
    print(admin.Info+language(lang)(2),inputs)
    
def hangman(lang):
    userTries=0
    inputs=[color.pink+'']
    word,clue=randomWord()
    mask=maskWord(word)
    while True:
        unMask="".join(mask)
        win= validate.userWin(lang, word, unMask)
        if win==True:
            break
        showImage(lang, clue, userTries, mask, inputs)
        print('\n')
        print(admin.Run+language(lang)(3),end=' ')
        letter=input(color.green+'')
        incognito=validate.userWin_or_Lose(lang, letter, word)
        if incognito=='userWin' or incognito==word:
            validate.userWin(lang, word, word)
            break
        elif incognito=='userLoss':
            validate.userLoss(lang, word)
            break
        prompt=validate.userInput(lang, letter, inputs, word)
        if prompt=='userLoss':
            validate.userLoss(lang, word)
            break
        win=validate.userWin(lang, word,prompt)
        if win==True:
            break
        inputs.append(prompt)
        inputs.append(',')
        if prompt in word:
            for i in range(len(word)):
                if word[i]==prompt:
                    mask[i]=prompt                     
            num=word.count(prompt)
            print()
            efects.Writer(admin.Good+language(lang)(4).format(str(num)) ,4)
            sleep(2)
        elif userTries==5:
            validate.userLoss(lang, word)
            break
        else:
            print()               
            efects.Writer(admin.Wrong+language(lang)(5),4)   
            sleep(1)
            userTries+=1        
        system("clear")
    
if __name__=='__main__':
    while True:
        print(' Hangman Game (', end=' ')
        lang=input(color.yellow+'En'+color.white+'glish | '+color.yellow+'Es'+color.white+'pañol ): '+color.green)
        print('\n')
        begining()
        language(lang)
        print()     
        print(rules.rules)
        hangman(lang)
        print('\n')             
        print(admin.Question+language(lang)(6)+color.yellow+'Y'+color.white+'es | '+color.yellow+'N'+color.white+'o')
        print()
        exitGame.exitGame(lang, admin.Run+' DecosSoft»» '+color.green)
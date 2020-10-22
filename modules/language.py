                
def language(lang):
    def english(var):
        game_lang={
                                0:' Number of Characters  ',
                                1:' Remaining tries: ',
                                2:' Input letters: ',
                                3: ' Input a letter: ',
                                4: ' Right! there are: {0}',
                                5:' Wrong letter!',
                                6:' Play again? ',
                                7:'\t★ You Win ',
                                8:'\n\tThe guess word is:',
                                9:'\n\t- G a m e  O v e r -',
                                10:' Make a guess: ',
                                11:' It\'s all ready inserted!',
                                12:' Try again: ',
                                13:' Wrong input!',
                                14:'\t★ You Loss ',
                                15:'\n\tThe guess word was: ',
                                16:' Wrong input, try again!\n',
                                17:' Thank you for playing this game...Have a nice day !',
                                18:' Initialization, wait a second.....\n',
                                19:' I think you don\'t want to continue...Good bye !'}
                                                             
        value=game_lang.get(var)
        return value
        
    def spanish(var):
        game_lang={
                                0:' Número de caracteres: ',
                                1:' Intentos restantes: ',
                                2:' Letras ingresadas: ',
                                3:' Ingresa una letra: ',
                                4: ' Bien! existe(n): {0}',
                                5:' Letra equivocada!',
                                6:' Jugar otra vez? ',
                                7:'\t★ Ganaste ',
                                8:'\n\tLa palabra fue:',
                                9:'\n\t- Juego Terminado -',
                                10:' Adivina la palabra: ',
                                11:' Letra ya ingresada!',
                                12:' Intenta otra vez: ',
                                13:' Entrada invalida!',
                                14:'\t★ Perdiste ',
                                15:'\n\tLa palabra secreta era: ',
                                16:' Entrada invalida!, Intenta nuevamente!\n',
                                17:' Gracias por jugar...Que tengas un buen día!',
                                18:' Inizializando, espera un segundo.....\n',
                                19:' Al parecer no deseas continuar...Adios!'}
                                
                                                          
        value=game_lang.get(var)
        return value
            
    lang_func={
                          'en':english,
                          'es':spanish}
                              
    return lang_func[lang]
class Ascii:
    g = grey = '\033[90m'
    pink = '\033[95m'
    cyan = '\033[96m'
    cyanOscuro = '\033[36m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    white = '\033[97m'
    red = '\033[91m'
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'
    
class Fg:
    Null = 0
    FgGrey =30
    FgRed = 91
    FgGreen = 92
    FgYellow = 93
    FgBlue = 34
    FgRosa= 95
    FgCyan = 96
    FgWhite = 97
    
class Bg:
    Null = 0
    BgGrey =100
    BgBlack= 40
    BgRed = 41
    BgGreen = 42
    BgYellow = 43
    BgBlue = 44
    BgRosa = 45
    BgCyan = 46
    BgWhite = 47
    
class Base:
    Null = 0
    B= Bold = 1
    U= Underline = 4
    M = Mask = 8
    #clean="\033[2Jsamples"#clear screen  

class Admin:
    Info= '\033[93m [i]\033[0m'
    Warning= '\033[91m [!]\033[0m'
    Plus= '\033[94m [+]\033[0m'
    Minus= '\033[91m [-]\033[0m'
    Good= '\033[92m [√]\033[0m'
    Wrong= '\033[91m [x]\033[0m'
    Question= '\033[93m [?]\033[0m'
    Run= '\033[97m [>]\033[0m'

def cprintLine(Base, Bg, Fg, simbol, mul):
    format='\033[{:d};{:d};{:d}m'+(simbol*mul)+'\033[0m'
    print(format.format(int(Base),int(Bg),int(Fg),simbol,int(mul)))
    
def cprint(Base, Bg, Fg, text):
    format='\033[{:d};{:d};{:d}m{!s}\033[0m'
    print(format.format(int(Base),int(Bg),int(Fg),text))
    
def cprintSimbol(Fg, text):
    format='\033[90m[\033[{:d}m{!s}\033[90m]\033[0m'
    print (format.format(int(Fg),text),end=' ')
    
def cprintXposition(x, text):
    format='\033[1C'*x+text
    print(format.format(int(x),text))

def cprintXYposition(x, y, text):
    format='\033[{:d};{:d}H{!s}\033[0m'
    print(format.format(int(x),int(y),text))
    
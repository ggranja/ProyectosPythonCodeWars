import sys
from Clases import Player
def main():
    return
# Welcome-------------------------------------------------------------------

def greet(language):
    d = {"english": "Welcome",
    "czech": "Vitejte",
    "danish": "Velkomst",
    "dutch": "Welkom",
    "estonian": "Tere tulemast",
    "finnish": "Tervetuloa",
    "flemish": "Welgekomen",
    "french": "Bienvenue",
    "german": "Willkommen",
    "irish": "Failte",
    "italian": "Benvenuto",
    "latvian": "Gaidits",
    "lithuanian": "Laukiamas",
    "polish": "Witamy",
    "spanish": "Bienvenido",
    "swedish": "Valkommen",
    "welsh": "Croeso"}
    if d.get(language)== None:
        return "Welcome"
    else:
        return d[language]
#--------------------------------------------------------------------------

# Duck_Duck_Goose ---------------------------------------------------------
def duck_duck_goose(lista,i):
    return lista[(i-1)%len(lista)].name
# -------------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(int(main() or 0))

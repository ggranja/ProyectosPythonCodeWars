import sys
from Clases import Player
def main():
    return
#

# Duck_Duck_Goose ---------------------------------------------------------
def duck_duck_goose(lista,i):
    return lista[(i-1)%len(lista)].name
# -------------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(int(main() or 0))

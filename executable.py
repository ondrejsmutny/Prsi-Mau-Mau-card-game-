# Sorry for using czech language instead of english
# Toto je spouštěcí soubor

import config
import game
import random

game.start()
while game.vyhodnot_hru() == "a":
    # Základní cyklus obsluhující průběh hry
    print("")
    game.vypis_hru()
    game.tah_hrace()
    game.dokonci_tah_hrace()
    if game.vyhodnot_hru() == "0":
        print("Vyhrává hráč")
        break
    game.hrana_karta = ""
    game.tah_pocitace(config.pocitac_1)    
    if game.vyhodnot_hru() == "1":
        print("Vyhrává počítač 1")
        break
    game.tah_pocitace(config.pocitac_2)    
    if game.vyhodnot_hru() == "2":
        print("Vyhrává počítač 2")
        break

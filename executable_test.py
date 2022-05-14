# Sorry for using czech language instead of english
# Toto je testovací spouštěcí soubor, který v průběhu hry dává nahlédnout do klíčových seznamů a proměnných

import config
import game
import random

game.start()
while game.vyhodnot_hru() == "a":
    # Základní cyklus obsluhující průběh hry
    print("balicek", config.balicek)
    print("hrac", config.hrac)
    print("PC1", config.pocitac_1)
    print("PC2", config.pocitac_2)
    print("stul", config.stul)
    print("barva", config.barva)
    print("sedma", config.sedma)
    print("eso", config.eso)
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

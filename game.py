import random
import config
import fnmatch

hrana_karta = ""

def start():
    # Rozdá karty na začátku hry
    random.shuffle(config.balicek)
    config.hrac.extend(config.balicek[-4:])
    del config.balicek[-4:]
    config.pocitac_1.extend(config.balicek[-4:])
    del config.balicek[-4:]
    config.pocitac_2.extend(config.balicek[-4:])
    del config.balicek[-4:]
    config.stul.append(config.balicek[-1])
    del config.balicek[-1]
    if config.stul[-1].split('-')[1] == "7":
        # Nastavení, aby hráč hrál sedmu nebo lízal, pokud první karta ve hře je sedma
        config.sedma = 1
    if config.stul[-1].split('-')[1] == "Eso":
        # Nastavení, aby hráč hrál eso nebo stál, pokud první karta ve hře je eso
        config.eso = 1
    if config.stul[-1].split('-')[1] == "Svrsek":
        # Nastavení, aby hraná barva byla barva svrška, pokud vní karta ve hře je svršek
        config.barva.append(config.stul[-1].split('-')[0])

def vypis_hru():
    # Vypíše stav hry
    print(f"Počítač 1 drží {len(config.pocitac_1)} karet.\nPočítač 2 drží {len(config.pocitac_2)} karet.\nNa stole je {config.stul[-1]}.\nV ruce máte {config.hrac}.")

def tah_hrace():
    # Zeptá se na tah hráče   
    vstup()
    if config.stul[-1].split('-')[1] == "Eso" and config.eso > 0:
        # Zajišťuje, aby hráč mohl volit kroky dle pravidel prší, pokud na stole je eso
        hrana_karta_hrac(config.cislo_karty)
        if vyhodnot_tah(hrana_karta) != "OK":
            # Možnosti hráče, pokud nezahraje eso
            while vyhodnot_tah(hrana_karta) != "OK":
                if config.cislo_karty == -1:
                    # Pokud hráč vybere, že stojí (volba -1), tak ukončí funkci
                    return                    
                while config.cislo_karty < 1:
                    if config.cislo_karty < 1:
                        # Zamezí hráči, aby lízal
                        print("Teď nemůžeš lízat.")
                        vstup()
                        if config.cislo_karty == -1:
                            break
                        continue
                if config.cislo_karty == -1:
                    return                    
                hrana_karta_hrac(config.cislo_karty)
                if vyhodnot_tah(hrana_karta) == "OK":
                    # Pokud hráč zahraje eso
                    config.stul.append(hrana_karta)
                    del config.hrac[config.cislo_karty - 1]
                    break
                print("Vybranou kartu nelze hrát.")
                vstup()
                hrana_karta_hrac(config.cislo_karty)
        elif vyhodnot_tah(hrana_karta) == "OK":
            config.stul.append(hrana_karta)
            del config.hrac[config.cislo_karty - 1]
            return       
    else:
        # Zajišťuje, aby hráč mohl volit kroky dle pravidel prší, pokud na stole není eso
        hrana_karta_hrac(config.cislo_karty)
        if vyhodnot_tah(hrana_karta) != "OK":
            # Zamezuje, aby hráč hrál kartu, kterou zrovna dle pravidel prší hrát nemůže
            while vyhodnot_tah(hrana_karta) != "OK":
                if config.cislo_karty == 0:
                    # Pokud hráč chce lízat
                    lizani(config.hrac)
                    return                    
                while config.cislo_karty < 0:
                    # Zamezuje, aby hráč stál, když na stole není eso
                    if config.cislo_karty < 0:
                        print("Teď nemůžeš stát.")
                        vstup()
                        if config.cislo_karty == 0:
                            lizani(config.hrac)
                            break
                if config.cislo_karty == 0:
                    break
                hrana_karta_hrac(config.cislo_karty)
                if vyhodnot_tah(hrana_karta) == "OK":
                    # Pokud hráč vybere kartu, kterou dle pravidel prší hrát může
                    config.stul.append(hrana_karta)
                    del config.hrac[config.cislo_karty - 1]
                    break
                print("Vybranou kartu nelze hrát.")
                vstup()
                hrana_karta_hrac(config.cislo_karty)
        elif vyhodnot_tah(hrana_karta) == "OK":
            config.stul.append(hrana_karta)
            del config.hrac[config.cislo_karty - 1]
            return        

def dokonci_tah_hrace():
    # Dodatečné kroky u speciálních karet hraných hráčem
    if config.cislo_karty == -1:
        # Pokud hráč stojí po vyložením esu, toto vyložené eso už nebude nutit dalšího hráče stát nebo hrát jen eso
        config.eso = 0
    if hrana_karta != "":
        if hrana_karta.split('-')[1] == "7":
            # Pokud hráč hrál sedmu, tak doplní počítadlo, aby další hráč, který sedmu mít nebude, lízal správný počet karet
            config.sedma += 1
        if hrana_karta.split('-')[1] == "Eso":
            # Pokud hráč hrál eso, tak doplní počítadlo, aby další hráč, který eso mít nebude, stál
            config.eso += 1
        if hrana_karta.split('-')[1] == "Svrsek":
            # Zeptá se, na jakou barvu chce hráč změnit po vyložení svrška. Tu potom doplní do seznamu config.barva
            while True:
                cislo_barvy = input("Napiš pořadové číslo barvy, na kterou chceš změnit (1 - 4) pro Červená, Zelená, Žalud, Kule:")
                try:
                    cislo_barvy = int(cislo_barvy)
                    while cislo_barvy > 4 or cislo_barvy < 1:
                        print("Vybrané číslo barvy je příliš vysoké nebo nízké")
                        cislo_barvy = int(input("Napiš pořadové číslo barvy, na kterou chceš změnit (1 - 4) pro Červená, Zelená, Žalud, Kule:"))
                    if cislo_barvy == 1:
                        config.barva.append("Cervena")
                        break
                    if cislo_barvy == 2:
                        config.barva.append("Zelena")
                        break
                    if cislo_barvy == 3:
                        config.barva.append("Zalud")
                        break
                    if cislo_barvy == 4:
                        config.barva.append("Kule")
                        break
                except ValueError:
                    print("Zadej číslo.")

def hrana_karta_hrac(cislo_karty):
    # Nastaví hranou kartu jako globální proměnnou a přiřadí do ní vybranou kartu
    global hrana_karta
    if cislo_karty > 0:
        hrana_karta = config.hrac[config.cislo_karty - 1]
    return hrana_karta

def vyhodnot_tah(hrana_karta):
    # Vyhodnotí správnost tažené karty
    if hrana_karta != "":
        if config.stul[-1].split('-')[1] == "7" and config.sedma > 0:
            # Pokud je na stole sedma a předchozí hráč nelízal, hráč může hrát jen sedmu
            if hrana_karta.split('-')[1] == "7":
                return "OK"
            else:
                return "NOK"
        elif config.stul[-1].split('-')[1] == "Eso" and config.eso > 0:
            # Pokud je na stole eso a předchozí hráč nestál, hráč může hrát jen eso
            if hrana_karta.split('-')[1] == "Eso":
                return "OK"
            else:
                return "NOK"
        elif hrana_karta.split('-')[1] == "Svrsek":
            # Svrška hráč může hrát kdykoliv, pokud na stole není aktivní sedma nebo eso
            return "OK"
        else:
            if config.stul[-1].split('-')[1] == "Svrsek":
                # Zajišťuje, aby hráč hrál správnou barvu, kterou zvolil předchozí hráč, když vyložil svrška
                if config.barva[-1] == hrana_karta.split('-')[0]:
                    return "OK"
                else:
                    return "NOK"
            elif config.stul[-1].split('-')[0] == hrana_karta.split('-')[0]:
                # Ověřuje, zda se hráč snaží hrát správnou barvu
                return "OK"
            elif config.stul[-1].split('-')[1] == hrana_karta.split('-')[1]:
                # Ověřuje, zda se hráč snaží hrát správnou hodnotu
                return "OK"
            else:
                return "NOK"
    else:
        return

def tah_pocitace(pocitac):
    # Zahraje tah počítače
    hledani_znaku = fnmatch.filter(pocitac, "*-" + config.stul[-1].split('-')[1])
    hledani_barvy = fnmatch.filter(pocitac, config.stul[-1].split('-')[0] + "-*")
    hledani_svrska = fnmatch.filter(pocitac, "*-Svrsek")
    hledani_sedmy = fnmatch.filter(pocitac, "*-7")
    barva_mezi_sedmami = fnmatch.filter(hledani_sedmy, config.stul[-1].split('-')[0] + "-*")
    hledani_esa = fnmatch.filter(pocitac, "*-Eso")
    barva_mezi_esy = fnmatch.filter(hledani_esa, config.stul[-1].split('-')[0] + "-*")
    # Sekce reakcí počítače, pokud jsou na stole aktivní speciální karty
    if config.stul[-1].split('-')[1] == "7" and config.sedma > 0:
        # Reakce počítače na sedmu dle pravidel prší
        if len(hledani_sedmy) > 0:
            vybrana_karta = hledani_sedmy[0]
            dokonci_tah_pocitace(pocitac, vybrana_karta)
        else:
            lizani(pocitac)
    elif config.stul[-1].split('-')[1] == "Eso" and config.eso > 0:
        # Reakce počítače na eso dle pravidel prší
        if len(hledani_esa) > 0:
            vybrana_karta = hledani_esa[0]
            dokonci_tah_pocitace(pocitac, vybrana_karta)
        else:
            config.eso = 0
            if pocitac == config.pocitac_1:
                print("Počítač 1 stojí")
            elif pocitac == config.pocitac_2:
                print("Počítač 2 stojí")       
            return pocitac
    elif config.stul[-1].split('-')[1] == "Svrsek":
        # Reakce počítače na svrška dle pravidel prší
        hledani_zmeny = fnmatch.filter(pocitac, config.barva[-1] + "-*")
        if len(hledani_zmeny) > 0:
            # Počítač se přednostně snaží zbavit nespeciální karty s barvou, kterou zvolil předchozí hráč, když vyložil svrška
            vybrana_karta = hledani_zmeny[0]
            dokonci_tah_pocitace(pocitac, vybrana_karta)
        elif len(hledani_svrska) > 0:
            # Pokud počítač nemá správnou barvu a má svrška, hraje svrška
            vybrana_karta = hledani_svrska[0]
            dokonci_tah_pocitace(pocitac, vybrana_karta)
        else:
            lizani(pocitac)
        hledani_zmeny.clear()
    # Sekce reakcí počítače, pokud nejsou na stole aktivní speciální karty
    elif len(hledani_sedmy) > 0 and len(barva_mezi_sedmami) > 0:
            # Počítač se snaží přednostně hrát sedmu, aby donutil další hráče lízat
            vybrana_karta = barva_mezi_sedmami[0]
            dokonci_tah_pocitace(pocitac, vybrana_karta) 
    elif len(hledani_esa) > 0 and len(barva_mezi_esy) > 0:
            # Počítač se snaží přednostně hrát eso, aby donutil další hráče stát
            vybrana_karta = barva_mezi_esy[0]
            dokonci_tah_pocitace(pocitac, vybrana_karta) 
    elif len(hledani_znaku) > 0 and hledani_znaku[0].split('-')[1] != "Svrsek":
        # Počítač hraje barvu, pokud ji má
        vybrana_karta = hledani_znaku[0]
        dokonci_tah_pocitace(pocitac, vybrana_karta)
    elif len(hledani_barvy) > 0 and hledani_barvy[0].split('-')[1] != "Svrsek":
        # Počítač hraje hodnotu, pokud ji má
        vybrana_karta = hledani_barvy[0]
        dokonci_tah_pocitace(pocitac, vybrana_karta)
    elif len(hledani_svrska) > 0:
        # Počítač hraje svrška, pokud ho má
        vybrana_karta = hledani_svrska[0]
        dokonci_tah_pocitace(pocitac, vybrana_karta)
    else:
        lizani(pocitac)
    hledani_znaku.clear()
    hledani_barvy.clear()  
    hledani_svrska.clear()
    hledani_sedmy.clear()
    barva_mezi_sedmami.clear()
    hledani_esa.clear()
    barva_mezi_esy.clear()
    return pocitac

def vyhodnot_hru():
    # Vyhodnotí stav hry, zda nějaký z hráčů neodhodil poslední kartu a nevyhrál tak
    if len(config.hrac) == 0:
        return "0"
    elif len(config.pocitac_1) == 0:
        return "1"
    elif len(config.pocitac_2) == 0:
        return "2"
    else:
        return "a"

def lizani(ruka_hrace):
    # Vyhodnotí balíček, zda není potřeba zamíchat, a potom lízne kartu
    if config.stul[-1].split('-')[1] == "7" and config.sedma > 0:
        # Zajišťuje, aby bylo nalízáno správného počtu karet, podle toho, kolik bylo vyloženo sedem a předchozí hráč nelízal
        while config.sedma > 0:
                if len(config.balicek) == 0:
                    # Pokud už není v balíčku žádná karta k líznutí, vezme všechny karty ze stolu kromě poslední, doplní je do balíčku a náhodně jej zamíchá
                    config.balicek.extend(config.stul[:-1])
                    del config.stul[:-1]
                    random.shuffle(config.balicek)
                ruka_hrace.append(config.balicek[-1])
                del config.balicek[-1]
                if len(config.balicek) == 0:
                    config.balicek.extend(config.stul[:-1])
                    del config.stul[:-1]
                    random.shuffle(config.balicek)
                ruka_hrace.append(config.balicek[-1])
                del config.balicek[-1]
                config.sedma -= 1
        if ruka_hrace == config.pocitac_1:
            print("Počítač 1 líže")
        elif ruka_hrace == config.pocitac_2:
            print("Počítač 2 líže")       
        return ruka_hrace
    else:
        if len(config.balicek) == 0:
            config.balicek.extend(config.stul[:-1])
            del config.stul[:-1]
            random.shuffle(config.balicek)
        ruka_hrace.append(config.balicek[-1])
        del config.balicek[-1]
        if ruka_hrace == config.pocitac_1:
            print("Počítač 1 líže")
        elif ruka_hrace == config.pocitac_2:
            print("Počítač 2 líže")       
        return ruka_hrace

def dokonci_tah_pocitace(pocitac, vybrana_karta):
    # Dokončí tah počítače po vybrané kartě
    config.stul.append(vybrana_karta)
    del pocitac[pocitac.index(vybrana_karta)]
    if pocitac == config.pocitac_1:
        print("Počítač 1 hraje", vybrana_karta)
    if pocitac == config.pocitac_2:
        print("Počítač 2 hraje", vybrana_karta)
    if vybrana_karta.split('-')[1] == "7":
        # Pokud počítač hrál sedmu, nastaví ji jako aktivní
        config.sedma += 1
    if vybrana_karta.split('-')[1] == "Eso":
        # Pokud počítač hrál eso, nastaví jej jako aktivní
        config.eso += 1
    if vybrana_karta.split('-')[1] == "Svrsek" and len(pocitac) > 0:
        # Pokud počítač hrál svrška, zjistí ze zbývajících karet, jakou barvu chce počítač zvolit a zvolí jí
        config.barva.append(pocitac[0].split('-')[0])
        print("Zvolená barva je", config.barva[-1])    
    return pocitac, vybrana_karta

def vstup():
    # Prověří správnost vstupu z hlediska srozumitelosti pro program
    while True:
        config.cislo_karty = input("Napiš pořadové číslo karty, kterou chceš hrát, 0 pro líznutí nebo -1, pokud stojíš:")
        try:
            config.cislo_karty = int(config.cislo_karty)
            while config.cislo_karty > len(config.hrac) or config.cislo_karty < -1:
                print("Vybrané číslo karty je příliš vysoké nebo nízké")
                config.cislo_karty = int(input("Napiš pořadové číslo karty, kterou chceš hrát, 0 pro líznutí nebo -1, pokud stojíš:"))
                if config.cislo_karty <= len(config.hrac) and config.cislo_karty >= -1:
                    return config.cislo_karty
                    break
            return config.cislo_karty
        except ValueError:
            print("Zadej číslo.")

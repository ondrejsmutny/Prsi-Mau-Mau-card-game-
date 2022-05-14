import game
import config

def test_vyhodnot_tah_1():
    # Test stejné barvy
    hrana_karta = "Kule-10"
    config.stul = ["Cervena-8", "Kule-8"]
    assert game.vyhodnot_tah(hrana_karta) == "OK"

def test_vyhodnot_tah_2():
    # Test stejné hodnoty
    hrana_karta = "Kule-10"
    config.stul = ["Cervena-8", "Zalud-10"]
    assert game.vyhodnot_tah(hrana_karta) == "OK"

def test_vyhodnot_tah_3():
    # Test nestejné barvy ani hodnoty
    hrana_karta = "Kule-10"
    config.stul = ["Cervena-8", "Zalud-Eso"]
    assert game.vyhodnot_tah(hrana_karta) == "NOK"

def test_vyhodnot_tah_4():
    # Test Svrška
    hrana_karta = "Kule-Svrsek"
    config.stul = ["Cervena-8", "Zalud-Spodek"]
    assert game.vyhodnot_tah(hrana_karta) == "OK"

def test_vyhodnot_tah_5():
    # Test správné barvy po Svrškovi
    hrana_karta = "Zelena-Spodek"
    config.stul = ["Cervena-8", "Zalud-Spodek", "Cervena-Svrsek"]
    config.barva = ["Zalud", "Zelena"]
    assert game.vyhodnot_tah(hrana_karta) == "OK"

def test_vyhodnot_tah_6():
    # Test špatné barvy po Svrškovi
    hrana_karta = "Zelena-Spodek"
    config.stul = ["Cervena-8", "Zalud-Spodek", "Cervena-Svrsek"]
    config.barva = ["Zalud", "Kule"]
    assert game.vyhodnot_tah(hrana_karta) == "NOK"

def test_vyhodnot_tah_7():
    # Test Svrška po Svrškovi
    hrana_karta = "Zelena-Svrsek"
    config.stul = ["Cervena-8", "Zalud-Spodek", "Cervena-Svrsek"]
    config.barva = ["Zalud", "Kule"]
    assert game.vyhodnot_tah(hrana_karta) == "OK"

def test_vyhodnot_tah_8():
    # Test Sedmy po Sedmě
    hrana_karta = "Cervena-7"
    config.stul = ["Cervena-8", "Zalud-7"]
    config.sedma = 1
    assert game.vyhodnot_tah(hrana_karta) == "OK"

def test_vyhodnot_tah_9():
    # Test barvy po Sedmě
    hrana_karta = "Zalud-Kral"
    config.stul = ["Cervena-8", "Zalud-7"]
    config.sedma = 1
    assert game.vyhodnot_tah(hrana_karta) == "NOK"

def test_tah_pocitace_1():
    # Test zahrání znaku
    pocitac = ["Kule-8", "Kule-10", "Cervena-Spodek", "Zelena-Kral"]
    config.stul = ["Cervena-Eso", "Zelena-10"]
    assert game.tah_pocitace(pocitac) == ["Kule-8", "Cervena-Spodek", "Zelena-Kral"]

def test_tah_pocitace_2():
    # Test zahrání barvy
    pocitac = ["Kule-8", "Kule-Spodek", "Cervena-Spodek", "Zelena-Kral"]
    config.stul = ["Cervena-Eso", "Zelena-10"]
    assert game.tah_pocitace(pocitac) == ["Kule-8", "Kule-Spodek","Cervena-Spodek"]

def test_tah_pocitace_3():
    # Test líznutí karty
    pocitac = ["Kule-8", "Kule-Spodek", "Cervena-Spodek", "Zalud-Kral"]
    config.stul = ["Cervena-Eso", "Zelena-10"]
    config.balicek = ["Zalud-8", "Zelena-Eso"]
    assert game.tah_pocitace(pocitac) == ["Kule-8", "Kule-Spodek", "Cervena-Spodek", "Zalud-Kral", "Zelena-Eso"]

def test_tah_pocitace_4():
    # Test zahrání Svrška
    pocitac = ["Kule-8", "Kule-Spodek", "Cervena-Svrsek", "Zalud-Kral"]
    config.stul = ["Cervena-Eso", "Zelena-10"]
    assert game.tah_pocitace(pocitac) == ["Kule-8", "Kule-Spodek", "Zalud-Kral"]

def test_tah_pocitace_5():
    # Test zahrání karty po Svrškovi
    pocitac = ["Kule-8", "Kule-Spodek", "Cervena-Svrsek", "Zalud-Kral"]
    config.stul = ["Cervena-Eso", "Zelena-Svrsek"]
    config.barva = ["Zelena", "Zalud"]
    assert game.tah_pocitace(pocitac) == ["Kule-8", "Kule-Spodek", "Cervena-Svrsek"]

def test_tah_pocitace_6():
    # Test zahrání Svrška po Svrškovi
    pocitac = ["Kule-8", "Kule-Spodek", "Cervena-Svrsek", "Zalud-Kral"]
    config.stul = ["Cervena-Eso", "Zelena-Svrsek"]
    config.barva = ["Zelena"]
    assert game.tah_pocitace(pocitac) == ["Kule-8", "Kule-Spodek", "Zalud-Kral"]

def test_tah_pocitace_7():
    # Test líznutí po Svrškovi
    pocitac = ["Kule-8", "Kule-Spodek", "Cervena-Spodek", "Zalud-Kral"]
    config.stul = ["Cervena-Eso", "Zelena-Svrsek"]
    config.barva = ["Zelena"]
    config.balicek = ["Zalud-Eso", "Zelena-9"]
    assert game.tah_pocitace(pocitac) == ["Kule-8", "Kule-Spodek", "Cervena-Spodek", "Zalud-Kral", "Zelena-9"]

def test_tah_pocitace_8():
    # Test zahrání sedmy přednostně před všemi kartami
    pocitac = ["Cervena-9", "Zelena-Kral", "Zelena-Svrsek", "Zelena-Eso", "Zelena-7"]
    config.stul = ["Zelena-Spodek"]
    assert game.tah_pocitace(pocitac) == ["Cervena-9", "Zelena-Kral", "Zelena-Svrsek", "Zelena-Eso"]

def test_tah_pocitace_9():
    # Test Sedmy po Sedme
    pocitac = ["Cervena-9", "Zelena-Kral", "Zelena-Svrsek", "Zelena-Eso", "Zelena-7"]
    config.stul = ["Cervena-7"]
    assert game.tah_pocitace(pocitac) == ["Cervena-9", "Zelena-Kral", "Zelena-Svrsek", "Zelena-Eso"]

def test_tah_pocitace_10():
    # Test lizani po Sedmě
    pocitac = ["Cervena-9", "Zelena-Kral"]
    config.stul = ["Kule-7", "Cervena-7"]
    config.balicek = ["Zelena-Svrsek", "Zelena-Eso", "Kule-Kral", "Cervena-Eso", "Zalud-8"]
    config.sedma = 2
    assert game.tah_pocitace(pocitac) == ["Cervena-9", "Zelena-Kral", "Zalud-8", "Cervena-Eso", "Kule-Kral", "Zelena-Eso"]

def test_tah_pocitace_11():
    # Test zahrání esa přednostně před vybranými kartami
    pocitac = ["Cervena-9", "Zelena-Kral", "Zelena-Svrsek", "Zelena-Eso"]
    config.stul = ["Zelena-Spodek"]
    assert game.tah_pocitace(pocitac) == ["Cervena-9", "Zelena-Kral", "Zelena-Svrsek"]

def test_tah_pocitace_12():
    # Test zahrání Esa po Esu
    pocitac = ["Kule-9", "Zelena-Kral", "Zelena-Svrsek", "Zelena-Eso"]
    config.stul = ["Kule-Eso"]
    config.eso = 1
    assert game.tah_pocitace(pocitac) == ["Kule-9", "Zelena-Kral", "Zelena-Svrsek"]

def test_tah_pocitace_13():
    # Test stání po Esu
    pocitac = ["Cervena-9", "Zelena-Kral", "Zelena-Svrsek"]
    config.stul = ["Kule-Eso"]
    config.eso = 1
    assert game.tah_pocitace(pocitac) == ["Cervena-9", "Zelena-Kral", "Zelena-Svrsek"]

def test_lizani_1():
    # Test zamíchání prázdného balíčku a líznutí karty
    config.balicek = []
    config.stul = ["Cervena-Eso", "Zalud-Eso"]
    hrac = ["Zelena-Eso"]
    assert game.lizani(hrac) == ["Zelena-Eso", "Cervena-Eso"]

def test_lizani_2():
    # Test lízání dvou karet po sedmě
    config.stul = ["Cervena-7"]
    config.sedma = 1
    config.balicek = ["Cervena-Eso", "Zelena-8", "Kule-Eso"]
    hrac = ["Zelena-10"]
    assert game.lizani(hrac) == ["Zelena-10", "Kule-Eso", "Zelena-8"]

def test_lizani_3():
    # Test lízání čtyř karet po sedmě
    config.stul = ["Cervena-7", "Zelena-7"]
    config.sedma = 2
    config.balicek = ["Cervena-Eso", "Zelena-8", "Kule-Eso", "Zalud-8", "Cervena-Kral"]
    hrac = ["Zelena-10"]
    assert game.lizani(hrac) == ["Zelena-10", "Cervena-Kral", "Zalud-8", "Kule-Eso", "Zelena-8"]

def test_lizani_4():
    # Test lízání šesti karet po sedmě
    config.stul = ["Cervena-7", "Zelena-7", "Kule-7"]
    config.sedma = 3
    config.balicek = ["Cervena-Eso", "Zelena-8", "Kule-Eso", "Zalud-8", "Cervena-Kral", "Zelena-9", "Kule-Kral"]
    hrac = ["Zelena-10"]
    assert game.lizani(hrac) == ["Zelena-10", "Kule-Kral", "Zelena-9", "Cervena-Kral", "Zalud-8", "Kule-Eso", "Zelena-8"]

def test_lizani_5():
    # Test lízání osmi karet po sedmě
    config.stul = ["Cervena-7", "Zelena-7", "Kule-7", "Zalud-7"]
    config.sedma = 4
    config.balicek = ["Cervena-Eso", "Zelena-8", "Kule-Eso", "Zalud-8", "Cervena-Kral", "Zelena-9", "Kule-Kral", "Zalud-9", "Cervena-Svrsek"]
    hrac = ["Zelena-10"]
    assert game.lizani(hrac) == ["Zelena-10", "Cervena-Svrsek", "Zalud-9", "Kule-Kral", "Zelena-9", "Cervena-Kral", "Zalud-8", "Kule-Eso", "Zelena-8"]

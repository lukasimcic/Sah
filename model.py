
zasedena_polja = {(1, 3): ('č', 'kraljica'), (4, 2): ('b', 'kralj'), (2, 2): ('b', 'tekač'), (2, 3): ('č', 'kralj'), (5, 7): ('b', 'kmet'), (6, 6): ('č', 'kmet')}

zasedena_polja_beli = {polje for polje in zasedena_polja if zasedena_polja[polje][0] == 'b'}
zasedena_polja_črni = {polje for polje in zasedena_polja if zasedena_polja[polje][0] == 'č'}

def svoja_polja_od(barva):  # da se izognem ponovnemu pisanju teh 4 vrstic
    if barva == 'b':
        return zasedena_polja_beli
    else:
        return zasedena_polja_črni
def nasprotnikova_polja_od(barva):
    if barva == 'b':
        return zasedena_polja_črni
    else:
        return zasedena_polja_beli

def na_katerih_poljih_je(figura, barva):  # to funkcijo bom potreboval kasneje
    množica = set()
    if barva == 'b':
        polja = zasedena_polja_beli
    else:
        polja = zasedena_polja_črni
    for polje in polja:
        if zasedena_polja[polje][1] == figura:
            množica.update({polje})  
    return množica

# možne poteze posameznih figur:


def poteze(figura, polje, barva):
    if figura == 'kmet':
        return poteze_kmet(polje, barva)
    if figura == 'trdnjava':
        return poteze_trdnjava(polje, barva)
    if figura == 'tekač':
        return poteze_tekač(polje, barva)
    if figura == 'konj':
        return poteze_konj(polje, barva)
    if figura == 'kraljica':
        return poteze_kraljica(polje, barva)
    else:
        return poteze_kralj(polje, barva)



def poteze_kmet_črni(polje):
    (v, s) = polje
    množica = set()

    if (v - 1, s - 1) in zasedena_polja_beli:
        množica.update({(v - 1, s - 1)})
    if (v - 1, s + 1) in zasedena_polja_beli:
        množica.update({(v - 1, s + 1)})
    
    if (v - 1, s) in zasedena_polja_črni:
        return množica

    if v == 2:
        množica.update({(1, s)})
        # se spremeni v kraljico
    if v == 7:
        množica.update({(6, s)}) 
        if (5, s) not in zasedena_polja_črni:
            množica.update({(5, s)}) 
    else:
        množica.update({(v - 1, s)})
    
    return množica



def poteze_kmet_beli(polje):
    (v, s) = polje
    množica = set()

    if (v + 1, s - 1) in zasedena_polja_črni:
        množica.update({(v - 1, s - 1)})
    if (v + 1, s + 1) in zasedena_polja_črni:
        množica.update({(v - 1, s + 1)})
    
    if (v + 1, s) in zasedena_polja_beli:
        return množica

    if v == 7:
        množica.update({(8, s)})
        # se spremeni v kraljico
    if v == 2:
        množica.update({(3, s)}) 
        if (4, s) not in zasedena_polja_beli:
            množica.update({(4, s)}) 
    else:
        množica.update({(v + 1, s)})
    
    return množica



def poteze_kmet(polje, barva):
    if barva == 'b':
        return poteze_kmet_beli(polje)
    else:
        return poteze_kmet_črni(polje)



def poteze_trdnjava(polje, barva):
    (v, s) = polje
    množica = set()
    nasprotnikova_polja = nasprotnikova_polja_od(barva)
    svoja_polja = svoja_polja_od(barva)
    
    # dol
    for i in range(1, v)[::-1]:
        if (i, s) in nasprotnikova_polja:
            množica.update({(i, s)})
            break
        if (i, s) in svoja_polja:
            break
        množica.update({(i, s)})

    # gor
    for i in range(v + 1, 9):
        if (i, s) in nasprotnikova_polja:
            množica.update({(i, s)})
            break
        if (i, s) in svoja_polja:
            break
        množica.update({(i, s)})

    # levo
    for i in range(1, s)[::-1]:
        if (v, i) in nasprotnikova_polja:
            množica.update({(v, i)})
            break
        if (v, i) in svoja_polja:
            break
        množica.update({(v, i)})

    # desno
    for i in range(s + 1, 9):
        if (v, i) in nasprotnikova_polja:
            množica.update({(v, i)})
            break
        if (v, i) in svoja_polja:
            break
        množica.update({(v, i)})
    
    return množica
    


def poteze_konj(polje, barva):
    (v, s) = polje
    množica = set()
    svoja_polja = svoja_polja_od(barva)

    for i in [2, -2]:
        for j in [1, -1]:

            # pogoj je, da na polju ni črne figure in da ne skoči iz plošče

            if not (v + i, s + j) in svoja_polja and 9 > v + i > 0 and 9 > s + j > 0:
                množica.update({(v + i, s + j)})
            if not (v + j, s + i) in svoja_polja and 9 > v + j > 0 and 9 > s + i > 0:
                množica.update({(v + j, s + i)})

    return množica



def poteze_tekač(polje, barva):
    (v, s) = polje
    množica = set()
    nasprotnikova_polja = nasprotnikova_polja_od(barva)
    svoja_polja = svoja_polja_od(barva)

    # desno gor
    for i in range(1, min(9 - v, 9 - s)):
        if (v + i, s + i) in nasprotnikova_polja:
            množica.update({(v + i, s + i)})
            break
        if (v + i, s + i) in svoja_polja:
            break
        množica.update({(v + i, s + i)}) 

    # desno dol
    for i in min(range(1, v), range(1, 9 - s), key=len):
        if (v - i, s + i) in nasprotnikova_polja:
            množica.update({(v - i, s + i)})
            break
        if (v - i, s + i) in svoja_polja:
            break
        množica.update({(v - i, s + i)})

    # levo gor
    for i in min(range(1, s), range(1, 9 - v), key=len):
        if (v + i, s - i) in nasprotnikova_polja:
            množica.update({(v + i, s - i)})
            break
        if (v + i, s - i) in svoja_polja:
            break
        množica.update({(v + i, s - i)})
    
    # levo dol
    for i in range(1, min(v, s)):
        if (v - i, s - i) in nasprotnikova_polja:
            množica.update({(v - i, s - i)})
            break
        if (v - i, s - i) in svoja_polja:
            break
        množica.update({(v - i, s - i)})

    return množica



def poteze_kraljica(polje, barva):
    return poteze_tekač(polje, barva).union(poteze_trdnjava(polje, barva))


# da vidimo, kam se kralj ne sme premakniti, moramo pogledati ogroženost figur (rabimo tudi še za naprej):

def računa_ogrožena_polja_za(barva):
    if barva == 'b':
        nasprotnikova_polja = zasedena_polja_črni
    else:
        nasprotnikova_polja = zasedena_polja_beli
    množica = set()

    for polje in nasprotnikova_polja:
        (v, s) = polje[0], polje[1]
        barva, figura = zasedena_polja[polje]

        if figura == 'kmet':
            if barva == 'b':
                množica.update({(v + 1, s + 1)})
                množica.update({(v + 1, s - 1)})
            else:
                množica.update({(v - 1, s + 1)})
                množica.update({(v - 1, s - 1)})

        elif figura == 'kralj':
            for i in [-1, 1, 0]:
                for j in [-1, 1, 0]:
                    if not j == 0 == i:
                        if not (v + i, s + j) in nasprotnikova_polja and 9 > v + i > 0 and 9 > s + j > 0:
                            množica.update({(v + i, s + j)})
                        if not (v - i, s - j) in nasprotnikova_polja and 9 > v - i > 0 and 9 > s - j > 0:
                            množica.update({(v - i, s - j)})

        else: 
            množica.update(poteze(figura, polje, barva))

    return množica


ogrožena_polja_za_bele = računa_ogrožena_polja_za('b')
ogrožena_polja_za_črne = računa_ogrožena_polja_za('č')

def ogrožena_polja_za(barva):
    if barva == 'b':
        return ogrožena_polja_za_bele
    else:
        return ogrožena_polja_za_črne

def poteze_kralj(polje, barva):
    (v, s) = polje
    množica = set()
    svoja_polja = svoja_polja_od(barva)
    ogrožena_polja = ogrožena_polja_za(barva)

    for i in [-1, 1, 0]:
        for j in [-1, 1, 0]:
            if not j == 0 == i:

                if not (v + i, s + j) in svoja_polja.union(množica, ogrožena_polja) and 9 > v + i > 0 and 9 > s + j > 0:
                    množica.update({(v + i, s + j)})
                if not (v - i, s - j) in svoja_polja.union(množica, ogrožena_polja) and 9 > v - i > 0 and 9 > s - j > 0:
                    množica.update({(v - i, s - j)})
    return množica


# kriteriji, po katerih se avalvira, kako dobra je situacija za barvo

def ogroženost(barva):
    ogroženost = 0
    polja = svoja_polja_od(barva)
    ogrožena_polja = ogrožena_polja_za(barva)
    for polje in polja:
        if polje in ogrožena_polja:
            ogroženost += 1
    return ogroženost

vrednosti_figur = {'kmet': 1,
                   'konj': 3,
                   'tekač': 3,
                   'trdnjava': 5,
                   'kraljica': 9}

def vrednost(barva):
    vrednost = 0
    polja = svoja_polja_od(barva)
    for polje in polja:
        figura = zasedena_polja[polje][1]
        if figura != 'kralj':
            vrednost += vrednosti_figur[figura]
    return vrednost

def zaprtost_kralja(barva):
    polje = na_katerih_poljih_je('kralj', barva).pop()
    return 8 - len(poteze_kralj(polje, barva))

def ogroženost_kralja(barva):
    polje = na_katerih_poljih_je('kralj', barva).pop()
    if polje in ogrožena_polja_za(barva):
        return 1
    else:
        return 0

def ogroženost_kraljice(barva):
    polje = na_katerih_poljih_je('kraljica', barva)
    if polje == set():
        return 0 
    if polje.pop() in ogrožena_polja_za(barva):
        return 1
    else:
        return 0

def zasedenost_centra(barva):
    zasedenost = 0
    polja = svoja_polja_od(barva)
    for v in range(3, 7):
        for s in range(3, 7):
            if (v, s) in polja:
                zasedenost += 1
    return zasedenost
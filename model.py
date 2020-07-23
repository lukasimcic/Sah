zasedena_polja = {(4, 2): ('b', 'kralj'), (2, 2): ('b', 'tekač'), (2, 3): ('č', 'kralj'), (5, 7): ('b', 'kmet')}

zasedena_polja_beli = [polje for polje in zasedena_polja if zasedena_polja[polje][0] == 'b']
zasedena_polja_črni = [polje for polje in zasedena_polja if zasedena_polja[polje][0] == 'č']


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
    seznam = []

    if (v - 1, s - 1) in zasedena_polja_beli:
        seznam.append((v - 1, s - 1))
    if (v - 1, s + 1) in zasedena_polja_beli:
        seznam.append((v - 1, s + 1))
    
    if (v - 1, s) in zasedena_polja_črni:
        return seznam

    if v == 2:
        seznam.append((1, s))
        # se spremeni v kraljico
    if v == 7:
        seznam.append((6, s)) 
        if (5, s) not in zasedena_polja_črni:
            seznam.append((5, s)) 
    else:
        seznam.append((v - 1, s))
    
    return seznam



def poteze_kmet_beli(polje):
    (v, s) = polje
    seznam = []

    if (v + 1, s - 1) in zasedena_polja_črni:
        seznam.append((v - 1, s - 1))
    if (v + 1, s + 1) in zasedena_polja_črni:
        seznam.append((v - 1, s + 1))
    
    if (v + 1, s) in zasedena_polja_beli:
        return seznam

    if v == 7:
        seznam.append((8, s))
        # se spremeni v kraljico
    if v == 2:
        seznam.append((3, s)) 
        if (4, s) not in zasedena_polja_beli:
            seznam.append((4, s)) 
    else:
        seznam.append((v + 1, s))
    
    return seznam



def poteze_kmet(polje, barva):
    if barva == 'b':
        return poteze_kmet_beli(polje)
    else:
        return poteze_kmet_črni(polje)



def poteze_trdnjava(polje, barva):
    (v, s) = polje
    seznam = []
    if barva == 'b':
        nasprotnikova_polja, svoja_polja = zasedena_polja_črni, zasedena_polja_beli
    else:
        nasprotnikova_polja, svoja_polja = zasedena_polja_beli, zasedena_polja_črni
    
    # dol
    for i in range(1, v)[::-1]:
        if (i, s) in nasprotnikova_polja:
            seznam.append((i, s))
            break
        if (i, s) in svoja_polja:
            break
        seznam.append((i, s))

    # gor
    for i in range(v + 1, 9):
        if (i, s) in nasprotnikova_polja:
            seznam.append((i, s))
            break
        if (i, s) in svoja_polja:
            break
        seznam.append((i, s))

    # levo
    for i in range(1, s)[::-1]:
        if (v, i) in nasprotnikova_polja:
            seznam.append((v, i))
            break
        if (v, i) in svoja_polja:
            break
        seznam.append((v, i))

    # desno
    for i in range(s + 1, 9):
        if (v, i) in nasprotnikova_polja:
            seznam.append((v, i))
            break
        if (v, i) in svoja_polja:
            break
        seznam.append((v, i))
    
    return seznam
    


def poteze_konj(polje, barva):
    (v, s) = polje
    seznam = []
    if barva == 'b':
        svoja_polja = zasedena_polja_beli
    else:
        svoja_polja = zasedena_polja_črni

    for i in [2, -2]:
        for j in [1, -1]:

            # pogoj je, da na polju ni črne figure in da ne skoči iz plošče

            if not (v + i, s + j) in svoja_polja and 9 > v + i > 0 and 9 > s + j > 0:
                seznam.append((v + i, s + j))
            if not (v + j, s + i) in svoja_polja and 9 > v + j > 0 and 9 > s + i > 0:
                seznam.append((v + j, s + i))

    return seznam



def poteze_tekač(polje, barva):
    (v, s) = polje
    seznam = []
    if barva == 'b':
        nasprotnikova_polja, svoja_polja = zasedena_polja_črni, zasedena_polja_beli
    else:
        nasprotnikova_polja, svoja_polja = zasedena_polja_beli, zasedena_polja_črni

    # desno gor
    for i in range(1, min(9 - v, 9 - s)):
        if (v + i, s + i) in nasprotnikova_polja:
            seznam.append((v + i, s + i))
            break
        if (v + i, s + i) in svoja_polja:
            break
        seznam.append((v + i, s + i)) 

    # desno dol
    for i in min(range(1, v), range(1, 9 - s), key=len):
        if (v - i, s + i) in nasprotnikova_polja:
            seznam.append((v - i, s + i))
            break
        if (v - i, s + i) in svoja_polja:
            break
        seznam.append((v - i, s + i))

    # levo gor
    for i in min(range(1, s), range(1, 9 - v), key=len):
        if (v + i, s - i) in nasprotnikova_polja:
            seznam.append((v + i, s - i))
            break
        if (v + i, s - i) in svoja_polja:
            break
        seznam.append((v + i, s - i))
    
    # levo dol
    for i in range(1, min(v, s)):
        if (v - i, s - i) in nasprotnikova_polja:
            seznam.append((v - i, s - i))
            break
        if (v - i, s - i) in svoja_polja:
            break
        seznam.append((v - i, s - i))

    return seznam



def poteze_kraljica(polje, barva):
    return poteze_tekač(polje, barva) + poteze_trdnjava(polje, barva)



def poteze_kralj(polje, barva):
    (v, s) = polje
    seznam = []
    if barva == 'b':
        ogrožena_polja, svoja_polja = ogrožena_polja_za_bele, zasedena_polja_beli
    else:
        ogrožena_polja, svoja_polja = ogrožena_polja_za_črne, zasedena_polja_črni

    for i in [-1, 1, 0]:
        for j in [-1, 1, 0]:
            if not j == 0 == i:
                if not (v + i, s + j) in svoja_polja + seznam and 9 > v + i > 0 and 9 > s + j > 0:
                    seznam.append((v + i, s + j))
                if not (v - i, s - j) in svoja_polja + seznam and 9 > v - i > 0 and 9 > s - j > 0:
                    seznam.append((v - i, s - j))
    return seznam


def ogrožena_polja_za(barva):
    if barva == 'b':
        nasprotnikova_polja = zasedena_polja_črni
    else:
        nasprotnikova_polja = zasedena_polja_beli
    seznam = []

    for polje in nasprotnikova_polja:
        barva, figura = zasedena_polja[polje]

        if figura == 'kmet':
            if barva == 'b':
                seznam.append((polje[0] + 1, polje[1] + 1))
                seznam.append((polje[0] + 1, polje[1] - 1))
            else:
                seznam.append((polje[0] - 1, polje[1] + 1))
                seznam.append((polje[0] - 1, polje[1] - 1))

        else: 
            seznam += poteze(figura, polje, barva)

    return seznam


ogrožena_polja_za_bele = ogrožena_polja_za('b')
ogrožena_polja_za_črne = ogrožena_polja_za('č')
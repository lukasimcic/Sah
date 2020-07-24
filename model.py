zasedena_polja = {(4, 2): ('b', 'kralj'), (2, 2): ('b', 'tekač'), (2, 3): ('č', 'kralj'), (5, 7): ('b', 'kmet')}

zasedena_polja_beli = {polje for polje in zasedena_polja if zasedena_polja[polje][0] == 'b'}
zasedena_polja_črni = {polje for polje in zasedena_polja if zasedena_polja[polje][0] == 'č'}


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
    if barva == 'b':
        nasprotnikova_polja, svoja_polja = zasedena_polja_črni, zasedena_polja_beli
    else:
        nasprotnikova_polja, svoja_polja = zasedena_polja_beli, zasedena_polja_črni
    
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
    if barva == 'b':
        svoja_polja = zasedena_polja_beli
    else:
        svoja_polja = zasedena_polja_črni

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
    if barva == 'b':
        nasprotnikova_polja, svoja_polja = zasedena_polja_črni, zasedena_polja_beli
    else:
        nasprotnikova_polja, svoja_polja = zasedena_polja_beli, zasedena_polja_črni

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
    return poteze_tekač(polje, barva) + poteze_trdnjava(polje, barva)


def poteze_kralj(polje, barva):
    (v, s) = polje
    množica = set()
    if barva == 'b':
        ogrožena_polja, svoja_polja = ogrožena_polja_za_bele, zasedena_polja_beli
    else:
        ogrožena_polja, svoja_polja = ogrožena_polja_za_črne, zasedena_polja_črni

    for i in [-1, 1, 0]:
        for j in [-1, 1, 0]:
            if not j == 0 == i:
                if not (v + i, s + j) in svoja_polja + množica + ogrožena_polja and 9 > v + i > 0 and 9 > s + j > 0:
                    množica.update({(v + i, s + j)})
                if not (v - i, s - j) in svoja_polja + množica + ogrožena_polja and 9 > v - i > 0 and 9 > s - j > 0:
                    množica.update({(v - i, s - j)})
    return množica


def ogrožena_polja_za(barva):
    if barva == 'b':
        nasprotnikova_polja, svoja_polja = zasedena_polja_črni, zasedena_polja_beli
    else:
        nasprotnikova_polja, svoja_polja = zasedena_polja_beli, zasedena_polja_črni
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
                        if not (v + i, s + j) in svoja_polja and 9 > v + i > 0 and 9 > s + j > 0:
                            množica.update({(v + i, s + j)})
                        if not (v - i, s - j) in svoja_polja and 9 > v - i > 0 and 9 > s - j > 0:
                            množica.update({(v - i, s - j)})

        else: 
            množica.update(poteze(figura, polje, barva))

    return množica


ogrožena_polja_za_bele = ogrožena_polja_za('b')
ogrožena_polja_za_črne = ogrožena_polja_za('č')
import model

def mreža(množica):
    mreža = '  __   __   __   __   __   __   __   __ '
    i = 8
    while i > 0:
        v_vrstici = dict()
        vrstica = '\n\n|'
        for (v, s) in množica:
            if v == i:
                if type(množica) == set:
                    v_vrstici[s] = 0
                else:
                    v_vrstici[s] = (množica[(v, s)])
        for j in range(1, 9):
            if j in v_vrstici:
                if type(množica) == set:
                    vrstica += ' XX |'
                else:
                    vrstica += ' ' + v_vrstici[j][0] + v_vrstici[j][1] + ' |'
            else:
                vrstica += '    |'
        mreža += vrstica + '\n  __   __   __   __   __   __   __   __ '
        i -= 1
    return mreža

def izpis_poraza(igra):
    return 'Žal si izgubil. Več sreče naslednjič!'

def izpis_zmage(igra):
    return f'Čestitam! Premagal si računalnik s težavnostno stopnjo {igra.težavnost}'

def izpis_igre(igra):
    return mreža(igra.postavitev)

def izpis_napačne_poteze(igra):
    return f'Prosim, izberite veljavna polja. Izbirate lahko med naslednjimi polji: {igra.nasprotnikova_polja}'

def začetni_vnos():
    barva1, težavnost1 = 0, 0
    barva = input('Izberite barvo: ')
    if barva == 'bela':
        barva1 = 'b'
    elif barva == 'črna':
        barva1 = 'č'
    else:
        barva1 = None
    težavnost = input('Izberite težavnostno stopnjo (1 - najlažja, 3 - najtežja): ')
    if težavnost in {'1', '2', '3'}:
        težavnost1 = int(težavnost)
    return (barva1, težavnost1)

def nabor_iz_niza(niz):
    sez = []
    for x in list(niz):
        if x.isalnum():
            sez.append(int(x))
    return tuple(sez)

def zahtevaj_vnos(igra):
    prejšnje = input('Polje, iz katerega želite premakniti figuro: ') 
    novo = input('Polje, na katerega želite premakniti figuro: ')
    return (nabor_iz_niza(prejšnje), nabor_iz_niza(novo))

def poženi():
    barva, težavnot = začetni_vnos()
    while barva is None or težavnot is None:
        print('Barvo izbiraš med belo in črno, težavnost pa med 1, 2 in 3.')
        barva, težavnot = začetni_vnos()
    
    igra = model.nova_igra(barva, težavnot)
    print(izpis_igre(igra))

    while True:
        
        polje, poteza = zahtevaj_vnos(igra)
        stanje = igra.naslednja_poteza(polje, poteza)

        while stanje == model.NAPAČNA_POTEZA:
            print(izpis_napačne_poteze(igra))
            polje, poteza = zahtevaj_vnos(igra)
            stanje = igra.naslednja_poteza(polje, poteza)
        
        print(izpis_igre(igra))

        print('Prosim, počakajte na potezo računalnika.')

        if stanje == model.ZMAGA:
            print(izpis_zmage(igra))
            break

        stanje = igra.poteza_računalnika()
        print(izpis_igre(igra))

        if stanje == model.PORAZ:
            print(izpis_poraza(igra))
            break

poženi()
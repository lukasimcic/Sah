BELI = 'b'
ČRNI = 'č'

KMET = 'P'
TRDNJAVA = 'R'
KONJ = 'N'
TEKAČ = 'B'
KRALJICA = 'Q'
KRALJ = 'K'

ZMAGA = 'W'
PORAZ = 'X'
REMI = 'O'

NAPAČNA_POTEZA = 'xx'

ZAČETEK = 'S'

# začetno stanje:

zasedena_polja = { (1, 1): (BELI, TRDNJAVA), (1, 2): (BELI, KONJ), (1, 3): (BELI, TEKAČ), (1, 4): (BELI, KRALJICA), (1, 5): (BELI, KRALJ), (1, 6): (BELI, TEKAČ), (1, 7): (BELI, KONJ), (1, 8): (BELI, TRDNJAVA),
(2, 1): (BELI, KMET), (2, 2): (BELI, KMET), (2, 3): (BELI, KMET), (2, 4): (BELI, KMET), (2, 5): (BELI, KMET), (2, 6): (BELI, KMET), (2, 7): (BELI, KMET), (2, 8): (BELI, KMET),
(7, 1): (ČRNI, KMET), (7, 2): (ČRNI, KMET), (7, 3): (ČRNI, KMET), (7, 4): (ČRNI, KMET), (7, 5): (ČRNI, KMET), (7, 6): (ČRNI, KMET), (7, 7): (ČRNI, KMET), (7, 8): (ČRNI, KMET),
(8, 1): (ČRNI, TRDNJAVA), (8, 2): (ČRNI, KONJ), (8, 3): (ČRNI, TEKAČ), (8, 4): (ČRNI, KRALJICA), (8, 5): (ČRNI, KRALJ), (8, 6): (ČRNI, TEKAČ), (8, 7): (ČRNI, KONJ), (8, 8): (ČRNI, TRDNJAVA)}

# razredi figur (vsi imajo metodo poteze, ki vrne množico vseh možnih potez iz danega polja, kralj in kmet imata še metodo ogroža, ki vrne množico vseh polj, ki ju ogrožata):

class trdnjava:

    def __init__(self, barva, polje, svoja_polja, nasprotnikova_polja):
        self.v, self.s = polje
        self.barva = barva
        self.nasprotnikova_polja = nasprotnikova_polja
        self.svoja_polja = svoja_polja

        
    def poteze(self):
        množica = set()

        # dol
        for i in range(1, self.v)[::-1]:
            if (i, self.s) in self.nasprotnikova_polja:
                množica.update({(i, self.s)})
                break
            if (i, self.s) in self.svoja_polja:
                break
            množica.update({(i, self.s)})

        # gor
        for i in range(self.v + 1, 9):
            if (i, self.s) in self.nasprotnikova_polja:
                množica.update({(i, self.s)})
                break
            if (i, self.s) in self.svoja_polja:
                break
            množica.update({(i, self.s)})

        # levo
        for i in range(1, self.s)[::-1]:
            if (self.v, i) in self.nasprotnikova_polja:
                množica.update({(self.v, i)})
                break
            if (self.v, i) in self.svoja_polja:
                break
            množica.update({(self.v, i)})

        # desno
        for i in range(self.s + 1, 9):
            if (self.v, i) in self.nasprotnikova_polja:
                množica.update({(self.v, i)})
                break
            if (self.v, i) in self.svoja_polja:
                break
            množica.update({(self.v, i)})

        return množica

class tekač:

    def __init__(self, barva, polje, svoja_polja, nasprotnikova_polja):
        self.v, self.s = polje
        self.nasprotnikova_polja = nasprotnikova_polja
        self.svoja_polja = svoja_polja

    def poteze(self):

        množica = set()

        # desno gor
        for i in range(1, min(9 - self.v, 9 - self.s)):
            if (self.v + i, self.s + i) in self.nasprotnikova_polja:
                množica.update({(self.v + i, self.s + i)})
                break
            if (self.v + i, self.s + i) in self.svoja_polja:
                break
            množica.update({(self.v + i, self.s + i)}) 

        # desno dol
        for i in min(range(1, self.v), range(1, 9 - self.s), key=len):
            if (self.v - i, self.s + i) in self.nasprotnikova_polja:
                množica.update({(self.v - i, self.s + i)})
                break
            if (self.v - i, self.s + i) in self.svoja_polja:
                break
            množica.update({(self.v - i, self.s + i)})

        # levo gor
        for i in min(range(1, self.s), range(1, 9 - self.v), key=len):
            if (self.v + i, self.s - i) in self.nasprotnikova_polja:
                množica.update({(self.v + i, self.s - i)})
                break
            if (self.v + i, self.s - i) in self.svoja_polja:
                break
            množica.update({(self.v + i, self.s - i)})
    
        # levo dol
        for i in range(1, min(self.v, self.s)):
            if (self.v - i, self.s - i) in self.nasprotnikova_polja:
                množica.update({(self.v - i, self.s - i)})
                break
            if (self.v - i, self.s - i) in self.svoja_polja:
                break
            množica.update({(self.v - i, self.s - i)})

        return množica

class konj:

    def __init__(self, barva, polje, svoja_polja, nasprotnikova_polja):
        self.v, self.s = polje
        self.nasprotnikova_polja = nasprotnikova_polja
        self.svoja_polja = svoja_polja

    def poteze(self):
        množica = set()

        for i in [2, -2]:
            for j in [1, -1]:

                # pogoj je, da na polju ni črne figure in da ne skoči iz plošče

                if not (self.v + i, self.s + j) in self.svoja_polja and 9 > self.v + i > 0 and 9 > self.s + j > 0:
                    množica.update({(self.v + i, self.s + j)})
                if not (self.v + j, self.s + i) in self.svoja_polja and 9 > self.v + j > 0 and 9 > self.s + i > 0:
                    množica.update({(self.v + j, self.s + i)})

        return množica

class kraljica:

    def __init__(self, barva, polje, svoja_polja, nasprotnikova_polja):
        self.v, self.s = polje
        self.barva = barva
        self.nasprotnikova_polja = nasprotnikova_polja
        self.svoja_polja = svoja_polja

    def poteze(self):
        diagonala = tekač(self.barva, (self.v, self.s), self.svoja_polja, self.nasprotnikova_polja).poteze()
        vodoravno_in_navpično = trdnjava(self.barva, (self.v, self.s), self.svoja_polja, self.nasprotnikova_polja).poteze()
        return diagonala.union(vodoravno_in_navpično)

class kmet:
    
    def __init__(self, barva, polje, svoja_polja, nasprotnikova_polja, zasedena_polja):
        self.v, self.s = polje
        self.barva = barva
        self.nasprotnikova_polja = nasprotnikova_polja
        self.svoja_polja = svoja_polja
        self.zasedena_polja = zasedena_polja
        if barva == BELI:
            self.premik = 1
            self.začetek = 2
        else:
            self.premik = - 1
            self.začetek = 7

    def ogroža(self):

        return {(self.v + self.premik, self.s + 1), (self.v + self.premik, self.s - 1)}

    def poteze(self):

        množica = set()

        if (self.v + self.premik, self.s - 1) in self.nasprotnikova_polja:
            množica.update({(self.v + self.premik, self.s - 1)})
        if (self.v + self.premik, self.s + 1) in self.nasprotnikova_polja:
            množica.update({(self.v + self.premik, self.s + 1)})

        if (self.v + self.premik, self.s) in zasedena_polja:
            return množica

        if self.v == self.začetek:
            množica.update({(self.začetek + self.premik, self.s)})
            if (self.začetek + 2 * self.premik, self.s) not in zasedena_polja:
                množica.update({(self.začetek + 2 * self.premik, self.s)})

        else:
            množica.update({(self.v + self.premik, self.s)})

        return množica

# zaradi kraljevih potez moram še pogledati ogrožena polja:

def poteze(figura, polje, barva, svoja_polja, nasprotnikova_polja, zasedena_polja):
    if figura == KMET:
        return kmet(barva, polje, svoja_polja, nasprotnikova_polja, zasedena_polja).poteze()
    if figura == TRDNJAVA:
        return trdnjava(barva, polje, svoja_polja, nasprotnikova_polja).poteze()
    if figura == TEKAČ:
        return tekač(barva, polje, svoja_polja, nasprotnikova_polja).poteze()
    if figura == KONJ:
        return konj(barva, polje, svoja_polja, nasprotnikova_polja).poteze()
    if figura == KRALJICA:
        return kraljica(barva, polje, svoja_polja, nasprotnikova_polja).poteze()
    else:
        return kralj(barva, polje, svoja_polja, nasprotnikova_polja, zasedena_polja).poteze()

def ogrožena_polja_za(barva, svoja_polja, nasprotnikova_polja, zasedena_polja):
    množica = set()

    for polje in nasprotnikova_polja:
        barva, figura = zasedena_polja[polje]

        if figura == KMET:
            množica.update(kmet(barva, polje, nasprotnikova_polja, svoja_polja, zasedena_polja).ogroža())

        elif figura == KRALJ:
            množica.update(kralj(barva, polje, nasprotnikova_polja, svoja_polja, zasedena_polja).ogroža())

        else: 
            množica.update(poteze(figura, polje, barva, nasprotnikova_polja, svoja_polja, zasedena_polja))

    return množica

class kralj:
        
    def __init__(self, barva, polje, svoja_polja, nasprotnikova_polja, zasedena_polja):
        self.v, self.s = polje
        self.barva = barva
        self.svoja_polja = svoja_polja
        self.nasprotnikova_polja = nasprotnikova_polja
        self.postavitev = zasedena_polja

    def ogroža(self):

        množica = set()

        for i in [-1, 1, 0]:
            for j in [-1, 1, 0]:
                if not j == 0 == i:

                    if not (self.v + i, self.s + j) in self.svoja_polja.union(množica) and 9 > self.v + i > 0 and 9 > self.s + j > 0:
                        množica.update({(self.v + i, self.s + j)})
                    if not (self.v - i, self.s - j) in self.svoja_polja.union(množica) and 9 > self.v - i > 0 and 9 > self.s - j > 0:
                        množica.update({(self.v - i, self.s - j)})
        
        return množica

    def poteze(self):

        return (self.ogroža()).difference(ogrožena_polja_za(self.barva, self.svoja_polja, self.nasprotnikova_polja, self.postavitev))

# kriteriji, po katerih se avalvira, kako dobra je situacija za barvo

def ogroženost(barva, svoja_polja, nasprotnikova_polja, zasedena_polja):
    ogroženost = 0
    ogrožena_polja = ogrožena_polja_za(barva, svoja_polja, nasprotnikova_polja, zasedena_polja)
    for polje in svoja_polja:
        if polje in ogrožena_polja:
            ogroženost += 1
    return ogroženost

vrednosti_figur = {KMET: 1,
                   KONJ: 3,
                   TEKAČ: 3,
                   TRDNJAVA: 5,
                   KRALJICA: 9}

def vrednost(barva, svoja_polja, zasedena_polja):
    vrednost = 0
    for polje in svoja_polja:
        figura = zasedena_polja[polje][1]
        if figura != KRALJ:
            vrednost += vrednosti_figur[figura]
    return vrednost

def na_katerih_poljih_je(figura, barva, zasedena_polja):  # to funkcijo bom potreboval pri naslednjih treh kriterijih
    for polje in zasedena_polja:
        if zasedena_polja[polje] == (barva, figura):
            return polje
    return set()

def zaprtost_kralja(barva, svoja_polja, nasprotnikova_polja, zasedena_polja):
    polje = na_katerih_poljih_je(KRALJ, barva, zasedena_polja)
    return len(kralj(barva, polje, svoja_polja, nasprotnikova_polja, zasedena_polja).poteze())

def ogroženost_kralja(barva, svoja_polja, nasprotnikova_polja, zasedena_polja):
    polje = na_katerih_poljih_je(KRALJ, barva, zasedena_polja)
    if polje in ogrožena_polja_za(barva, svoja_polja, nasprotnikova_polja, zasedena_polja):
        return 2
    else:
        return 0

def ogroženost_kraljice(barva, svoja_polja, nasprotnikova_polja, zasedena_polja):
    polje = na_katerih_poljih_je(KRALJICA, barva, zasedena_polja)
    if polje == set():
        return 0 
    if polje in ogrožena_polja_za(barva, svoja_polja, nasprotnikova_polja, zasedena_polja):
        return 2
    else:
        return 0

def zasedenost_centra(barva, svoja_polja):
    zasedenost = 0
    for v in range(3, 7):
        for s in range(3, 7):
            if (v, s) in svoja_polja:
                zasedenost += 1
    return zasedenost

def zmaga(nasprotnikova_barva, zasedena_polja):
    return (nasprotnikova_barva, KRALJ) not in zasedena_polja.values()

# rang kriterijev, da vem, kako utežiti kriterije pri evalvaciji:
#   ogroženost: 0 - 16                  boljše manjše
#   vrednost: 0 - 36                    boljše večje
#   zaprtost_kralja: 0 - 8              boljše večje
#   ogroženost_kralja: 0 - 2            boljše manjše  
#   ogroženost_kraljice: 0 - 2          boljše manjše
#   zasedenost_centra: 0 - 16           boljše večje

def evalvacija(barva, svoja_polja, nasprotnikova_polja, zasedena_polja):
    if barva == BELI:
        nasprotna_barva = ČRNI
    else:
        nasprotna_barva = BELI

    evalvacija = 0

    evalvacija += - ogroženost(barva, svoja_polja, nasprotnikova_polja, zasedena_polja) + ogroženost(nasprotna_barva, nasprotnikova_polja, svoja_polja, zasedena_polja)
    
    evalvacija += (vrednost(barva, svoja_polja, zasedena_polja) - vrednost(nasprotna_barva, nasprotnikova_polja, zasedena_polja)) * 2
    
    evalvacija += (zaprtost_kralja(barva, svoja_polja, nasprotnikova_polja, zasedena_polja) - zaprtost_kralja(nasprotna_barva, nasprotnikova_polja, svoja_polja, zasedena_polja)) / 2
    
    evalvacija += - (ogroženost_kralja(barva, svoja_polja, nasprotnikova_polja, zasedena_polja) - ogroženost_kralja(nasprotna_barva, nasprotnikova_polja, svoja_polja, zasedena_polja)) * 4
    
    evalvacija += - (ogroženost_kraljice(barva, svoja_polja, nasprotnikova_polja, zasedena_polja) - ogroženost_kraljice(nasprotna_barva, nasprotnikova_polja, svoja_polja, zasedena_polja)) * 3
    
    evalvacija += (zasedenost_centra(barva, svoja_polja) - zasedenost_centra(nasprotna_barva, nasprotnikova_polja)) / 4

    return evalvacija

class igra:

    def __init__(self, barva, težavnost):
        self.barva = barva  # ta barva pripada računalniku
        self.nasprotnikova_barva = {BELI, ČRNI}.difference({barva}).pop()  # ta barva pripada igralcu
        self.postavitev = zasedena_polja
        self.svoja_polja = {polje for polje in self.postavitev if self.postavitev[polje][0] == barva}
        self.nasprotnikova_polja = set(zasedena_polja.keys()).difference(self.svoja_polja)
        self.težavnost = težavnost

    def najboljša_poteza(self):
        najboljša_ocena = self.težavnost * (-100)
        iskano_polje, iskana_poteza = 0, 0
        test = True # ta test se uporabi v primeru, da je v drugem koraku računalnikovega razmišljanja pojeden kralj

        for polje in self.svoja_polja:
            figura = self.postavitev[polje][1]

            for poteza in poteze(figura, polje, self.barva, self.svoja_polja, self.nasprotnikova_polja, self.postavitev):

                nova_postavitev = self.postavitev.copy()
                par = nova_postavitev.pop(polje)
                nova_postavitev[poteza] = par
                
                nova_svoja_polja = {polje for polje in nova_postavitev if nova_postavitev[polje][0] == self.barva}
                nova_nasprotnikova_polja = set(nova_postavitev.keys()).difference(nova_svoja_polja)  # ker je lahko kakšna nasprotnikova figura pojedena
                
                if zmaga(self.nasprotnikova_barva, nova_postavitev):
                    return (polje, poteza)

                ocena = evalvacija(self.barva, nova_svoja_polja, nova_nasprotnikova_polja, nova_postavitev)

                if self.težavnost > 1:
                    končna_ocena1 = 1000   # to bo evalvacija najslabse mozne poteze igralca za računalnik, ko igralec igra iz nove postavitve (raven 2) 

                    for polje1 in nova_nasprotnikova_polja:
                        figura = nova_postavitev[polje1][1]

                        for poteza1 in poteze(figura, polje1, self.nasprotnikova_barva, nova_nasprotnikova_polja, nova_svoja_polja, nova_postavitev):

                            nova_postavitev1 = nova_postavitev.copy()
                            par1 = nova_postavitev1.pop(polje1)
                            nova_postavitev1[poteza1] = par1

                            nova_svoja_polja1 = {polje for polje in nova_postavitev1 if nova_postavitev1[polje][0] == self.barva}
                            nova_nasprotnikova_polja1 = set(nova_postavitev1.keys()).difference(nova_svoja_polja1)  # ker je lahko kakšna nasprotnikova figura pojedena

                            if zmaga(self.barva, nova_postavitev1):
                                ocena1 = -101
                                ocena2 = 0
                                test = False

                            if self.težavnost == 2:
                                ocena1 = evalvacija(self.barva, nova_svoja_polja1, nova_nasprotnikova_polja1, nova_postavitev1)
                                končna_ocena1 = min(končna_ocena1, ocena1)  # najslabši mozen odziv igralca

                            if self.težavnost == 3 and test:
                                končna_ocena2 = -1000   # to bo evalvacija najboljše možne poteze računalnika, po tem ko se je igralec že odzval na potezo računalnika

                                for polje2 in nova_svoja_polja1:
                                    figura = nova_postavitev1[polje2][1]

                                    for poteza2 in poteze(figura, polje2, self.barva, nova_svoja_polja1, nova_nasprotnikova_polja1, nova_postavitev1):

                                        nova_postavitev2 = nova_postavitev1.copy()
                                        par2 = nova_postavitev2.pop(polje2)
                                        nova_postavitev2[poteza2] = par2

                                        nova_svoja_polja2 = {polje for polje in nova_postavitev2 if nova_postavitev2[polje][0] == self.barva}
                                        nova_nasprotnikova_polja2 = set(nova_postavitev2.keys()).difference(nova_svoja_polja2)  # ker je lahko kakšna nasprotnikova figura pojedena
                                        
                                        if zmaga(self.nasprotnikova_barva, nova_postavitev2):
                                            ocena2 = 20
                                        else:
                                            ocena2 = evalvacija(self.barva, nova_svoja_polja2, nova_nasprotnikova_polja2, nova_postavitev2)

                                        končna_ocena2 = max(končna_ocena2, ocena2)
                                
                                končna_ocena1 = min(končna_ocena2, končna_ocena1)

                    if najboljša_ocena < končna_ocena1:
                        iskano_polje, iskana_poteza = polje, poteza
                        najboljša_ocena = končna_ocena1

                else:
                    if najboljša_ocena < ocena:
                        iskano_polje, iskana_poteza = polje, poteza
                        najboljša_ocena = ocena                   

        return (iskano_polje, iskana_poteza)
                                                
    def naslednja_poteza(self, prejšnje_polje, novo_polje):

        if prejšnje_polje not in self.nasprotnikova_polja or novo_polje not in poteze(self.postavitev[prejšnje_polje][1], prejšnje_polje, self.nasprotnikova_barva, self.nasprotnikova_polja, self.svoja_polja, self.postavitev):
            return NAPAČNA_POTEZA

        elif prejšnje_polje == 0:
            return REMI

        else:

            (a, b) = self.postavitev.pop(prejšnje_polje)

            if b == KMET and novo_polje[0] == 8 or novo_polje[0] == 1:
                self.postavitev[novo_polje] = (a, KRALJICA)  # kmet se spremeni v kraljico  
            else:
                self.postavitev[novo_polje] = (a, b)

            self.svoja_polja = {polje for polje in self.postavitev if self.postavitev[polje][0] == self.barva}
            self.nasprotnikova_polja = set(zasedena_polja.keys()).difference(self.svoja_polja)

            if zmaga(self.nasprotnikova_barva, zasedena_polja):
                return PORAZ
            if zmaga(self.barva, zasedena_polja):
                return ZMAGA

    def poteza_računalnika(self):       

        (prejšnje_polje, novo_polje) = self.najboljša_poteza()
        (c, d) = self.postavitev.pop(prejšnje_polje)
        
        if d == KMET and novo_polje[0] == 8 or novo_polje[0] == 1:
            self.postavitev[novo_polje] = (c, KRALJICA)  # kmet se spremeni v kraljico  
        else:
            self.postavitev[novo_polje] = (c, d)
        
        self.svoja_polja = {polje for polje in self.postavitev if self.postavitev[polje][0] == self.barva}
        self.nasprotnikova_polja = set(zasedena_polja.keys()).difference(self.svoja_polja)
        if zmaga(self.nasprotnikova_barva, zasedena_polja):
            return PORAZ
        if zmaga(self.barva, zasedena_polja):
            return ZMAGA

def nova_igra(barva, težavnost):
    nasprotnikova_barva = {BELI, ČRNI}.difference({barva}).pop()
    return igra(nasprotnikova_barva, težavnost)

class sah:

    def __init__(self):
        self.igre = {}

    def prost_id_igre(self):
        if self.igre == {}:
            return 0
        else:
            return max(self.igre.keys()) + 1

    def nova_igra(self, barva, težavnost):
        id_igre = self.prost_id_igre()
        igra = nova_igra(barva, težavnost)
        self.igre[id_igre] = ((igra, barva, težavnost), ZAČETEK)
        return id_igre

    def poteza_igralca(self, id_igre, polje, poteza):
        igra, barva, težavnost = self.igre[id_igre][0]
        novo_stanje = igra.naslednja_poteza(polje, poteza)
        self.igre[id_igre][1] = (igra, barva, težavnost, novo_stanje)

    def poteza_računalnika(self, id_igre):
        igra, barva, težavnost = self.igre[id_igre][0]
        novo_stanje = igra.poteza_računalnika()
        self.igre[id_igre][1] = (igra, barva, težavnost, novo_stanje)

ZMAGA = 'W'
PORAZ = 'X'
REMI = 'O'

NAPAČNA_POTEZA = 'xx'

# začetno stanje:

zasedena_polja = { (1, 1): ('b', 'R'), (1, 2): ('b', 'N'), (1, 3): ('b', 'B'), (1, 4): ('b', 'Q'), (1, 5): ('b', 'K'), (1, 6): ('b', 'B'), (1, 7): ('b', 'N'), (1, 8): ('b', 'R'),
(2, 1): ('b', 'P'), (2, 2): ('b', 'P'), (2, 3): ('b', 'P'), (2, 4): ('b', 'P'), (2, 5): ('b', 'P'), (2, 6): ('b', 'P'), (2, 7): ('b', 'P'), (2, 8): ('b', 'P'),
(7, 1): ('č', 'P'), (7, 2): ('č', 'P'), (7, 3): ('č', 'P'), (7, 4): ('č', 'P'), (7, 5): ('č', 'P'), (7, 6): ('č', 'P'), (7, 7): ('č', 'P'), (7, 8): ('č', 'P'),
(8, 1): ('č', 'R'), (8, 2): ('č', 'N'), (8, 3): ('č', 'B'), (8, 4): ('č', 'Q'), (8, 5): ('č', 'K'), (8, 6): ('č', 'B'), (8, 7): ('č', 'N'), (8, 8): ('č', 'R')}

# razredi figur (vsi imajo metodo poteze, ki vrne množico vseh možnih potez iz danega polja, kralj in kmet imata še metodo ogroža, ki vrne množico vseh polj, ki ju ogrožata):

class R:

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

class B:

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

class N:

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

class Q:

    def __init__(self, barva, polje, svoja_polja, nasprotnikova_polja):
        self.v, self.s = polje
        self.barva = barva
        self.nasprotnikova_polja = nasprotnikova_polja
        self.svoja_polja = svoja_polja

    def poteze(self):
        diagonala = B(self.barva, (self.v, self.s), self.svoja_polja, self.nasprotnikova_polja).poteze()
        vodoravno_in_navpično = R(self.barva, (self.v, self.s), self.svoja_polja, self.nasprotnikova_polja).poteze()
        return diagonala.union(vodoravno_in_navpično)

class P:
    
    def __init__(self, barva, polje, svoja_polja, nasprotnikova_polja):
        self.v, self.s = polje
        self.barva = barva
        self.nasprotnikova_polja = nasprotnikova_polja
        self.svoja_polja = svoja_polja
        if barva == 'b':
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
            if (self.začetek + self.premik) not in self.svoja_polja:
                množica.update({(self.začetek + 2 * self.premik, self.s)})

        else:
            množica.update({(self.v + self.premik, self.s)})

        return množica

# zaradi kraljevih potez moram še pogledati ogrožena polja:

def poteze(figura, polje, barva, svoja_polja, nasprotnikova_polja, zasedena_polja):
    if figura == 'P':
        return P(barva, polje, svoja_polja, nasprotnikova_polja).poteze()
    if figura == 'R':
        return R(barva, polje, svoja_polja, nasprotnikova_polja).poteze()
    if figura == 'B':
        return B(barva, polje, svoja_polja, nasprotnikova_polja).poteze()
    if figura == 'N':
        return N(barva, polje, svoja_polja, nasprotnikova_polja).poteze()
    if figura == 'Q':
        return Q(barva, polje, svoja_polja, nasprotnikova_polja).poteze()
    else:
        return K(barva, polje, svoja_polja, nasprotnikova_polja, zasedena_polja).poteze()

def ogrožena_polja_za(barva, svoja_polja, nasprotnikova_polja, zasedena_polja):
    množica = set()

    for polje in nasprotnikova_polja:
        barva, figura = zasedena_polja[polje]

        if figura == 'P':
            množica.update(P(barva, polje, svoja_polja, nasprotnikova_polja).ogroža())

        elif figura == 'K':
            množica.update(K(barva, polje, svoja_polja, nasprotnikova_polja, zasedena_polja).ogroža())

        else: 
            množica.update(poteze(figura, polje, barva, svoja_polja, nasprotnikova_polja, zasedena_polja))

    return množica

class K:
        
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

vrednosti_figur = {'P': 1,
                   'N': 3,
                   'B': 3,
                   'R': 5,
                   'Q': 9}

def vrednost(barva, svoja_polja, zasedena_polja):
    vrednost = 0
    for polje in svoja_polja:
        figura = zasedena_polja[polje][1]
        if figura != 'K':
            vrednost += vrednosti_figur[figura]
    return vrednost

def na_katerih_poljih_je(figura, barva, zasedena_polja):  # to funkcijo bom potreboval pri naslednjih treh kriterijih
    for polje in zasedena_polja:
        if zasedena_polja[polje] == (barva, figura):
            return polje
    return set()

def zaprtost_kralja(barva, svoja_polja, nasprotnikova_polja, zasedena_polja):
    polje = na_katerih_poljih_je('K', barva, zasedena_polja)
    return len(K(barva, polje, svoja_polja, nasprotnikova_polja, zasedena_polja).poteze())

def ogroženost_kralja(barva, svoja_polja, nasprotnikova_polja, zasedena_polja):
    polje = na_katerih_poljih_je('K', barva, zasedena_polja)
    if polje in ogrožena_polja_za(barva, svoja_polja, nasprotnikova_polja, zasedena_polja):
        return 2
    else:
        return 0

def ogroženost_kraljice(barva, svoja_polja, nasprotnikova_polja, zasedena_polja):
    polje = na_katerih_poljih_je('Q', barva, zasedena_polja)
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
    return (nasprotnikova_barva, 'K') not in zasedena_polja.values()

# rang kriterijev, da vem, kako utežiti kriterije pri evalvaciji:
#   ogroženost: 0 - 16                  boljše manjše
#   vrednost: 0 - 36                    boljše večje
#   zaprtost_kralja: 0 - 8              boljše večje
#   ogroženost_kralja: 0 - 1            boljše manjše  
#   ogroženost_kraljice: 0 - 1          boljše manjše
#   zasedenost_centra: 0 - 16           boljše večje

def evalvacija(barva, svoja_polja, nasprotnikova_polja, zasedena_polja):
    if barva == 'b':
        nasprotna_barva = 'č'
    else:
        nasprotna_barva = 'b'

    evalvacija = 0

    evalvacija += - (ogroženost(barva, svoja_polja, nasprotnikova_polja, zasedena_polja) - ogroženost(nasprotna_barva, nasprotnikova_polja, svoja_polja, zasedena_polja))
    
    + (vrednost(barva, svoja_polja, zasedena_polja) - vrednost(nasprotna_barva, nasprotnikova_polja, zasedena_polja)) * 3 / 4
    
    + (zaprtost_kralja(barva, svoja_polja, nasprotnikova_polja, zasedena_polja) - zaprtost_kralja(nasprotna_barva, nasprotnikova_polja, svoja_polja, zasedena_polja)) * 2
    
    - (ogroženost_kralja(barva, svoja_polja, nasprotnikova_polja, zasedena_polja) - ogroženost_kralja(nasprotna_barva, nasprotnikova_polja, svoja_polja, zasedena_polja)) * 16
    
    - (ogroženost_kraljice(barva, svoja_polja, nasprotnikova_polja, zasedena_polja) - ogroženost_kraljice(nasprotna_barva, nasprotnikova_polja, svoja_polja, zasedena_polja)) * 8
    
    + (zasedenost_centra(barva, svoja_polja) - zasedenost_centra(nasprotna_barva, nasprotnikova_polja)) / 2

    return evalvacija
 
class igra:

    def __init__(self, barva, težavnost):
        self.barva = barva  # ta barva pripada računalniku
        self.nasprotnikova_barva = {'b', 'č'}.difference({barva}).pop()  # ta barva pripada igralcu
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
                #print(polje, poteza)

                nova_postavitev = self.postavitev.copy()
                par = nova_postavitev.pop(polje)
                nova_postavitev[poteza] = par
                
                nova_svoja_polja = {polje for polje in nova_postavitev if nova_postavitev[polje][0] == self.barva}
                nova_nasprotnikova_polja = set(nova_postavitev.keys()).difference(nova_svoja_polja)  # ker je lahko kakšna nasprotnikova figura pojedena
                
                if zmaga(self.nasprotnikova_barva, nova_postavitev):
                    return (polje, poteza)

                ocena = evalvacija(self.barva, nova_svoja_polja, nova_nasprotnikova_polja, nova_postavitev)

                if self.težavnost > 1:
                    
                    for polje1 in nova_nasprotnikova_polja:
                        figura = nova_postavitev[polje1][1]

                        for poteza1 in poteze(figura, polje1, self.nasprotnikova_barva, nova_nasprotnikova_polja, nova_svoja_polja, nova_postavitev):
                            #print('    ', polje1, poteza1)
                
                            nova_postavitev1 = nova_postavitev.copy()
                            par1 = nova_postavitev1.pop(polje1)
                            nova_postavitev1[poteza1] = par1

                            nova_svoja_polja1 = {polje for polje in nova_postavitev1 if nova_postavitev1[polje][0] == self.barva}
                            nova_nasprotnikova_polja1 = set(nova_postavitev1.keys()).difference(nova_svoja_polja1)  # ker je lahko kakšna nasprotnikova figura pojedena

                            if zmaga(self.barva, nova_postavitev1):
                                ocena1 = -101
                                ocena2 = 0
                                test = False

                            else:
                                ocena1 = evalvacija(self.barva, nova_svoja_polja1, nova_nasprotnikova_polja1, nova_postavitev1)

                            if self.težavnost == 3 and test:
                                
                                for polje2 in nova_svoja_polja1:
                                    figura = nova_postavitev1[polje2][1]

                                    for poteza2 in poteze(figura, polje2, self.barva, nova_svoja_polja1, nova_nasprotnikova_polja1, nova_postavitev1):
                                        #print('        ', polje2, poteza2)

                                        nova_postavitev2 = nova_postavitev1.copy()
                                        par2 = nova_postavitev2.pop(polje2)
                                        nova_postavitev2[poteza2] = par2

                                        nova_svoja_polja2 = {polje for polje in nova_postavitev2 if nova_postavitev2[polje][0] == self.barva}
                                        nova_nasprotnikova_polja2 = set(nova_postavitev2.keys()).difference(nova_svoja_polja2)  # ker je lahko kakšna nasprotnikova figura pojedena
                                        
                                        if zmaga(self.nasprotnikova_barva, nova_postavitev2):
                                            ocena2 = 20
                                        else:
                                            ocena2 = evalvacija(self.barva, nova_svoja_polja2, nova_nasprotnikova_polja2, nova_postavitev2)

                                        # ali je ta poteza najboljša do sedaj?

                                        končna_ocena = ocena + ocena1 + ocena2
                                        if najboljša_ocena < končna_ocena:
                                            iskano_polje, iskana_poteza = polje, poteza
                                            najboljša_ocena = končna_ocena

                            else:
                                končna_ocena = ocena + ocena1
                                if najboljša_ocena < končna_ocena:
                                    iskano_polje, iskana_poteza = polje, poteza
                                    najboljša_ocena = končna_ocena


                else:
                    if najboljša_ocena < ocena:
                        iskano_polje, iskana_poteza = polje, poteza
                        najboljša_ocena = ocena                   

        return (iskano_polje, iskana_poteza)
                                                
    def naslednja_poteza(self, prejšnje_polje, novo_polje):

        # najprej poteza, ki jo naredi igralec

        if prejšnje_polje not in self.nasprotnikova_polja or novo_polje not in poteze(self.postavitev[prejšnje_polje][1], prejšnje_polje, self.nasprotnikova_barva, self.nasprotnikova_polja, self.svoja_polja, self.postavitev):
            return NAPAČNA_POTEZA

        elif prejšnje_polje == 0:
            return REMI

        else:

            (a, b) = self.postavitev.pop(prejšnje_polje)

            if b == 'P' and novo_polje[0] == 8 or novo_polje[0] == 1:
                self.postavitev[novo_polje] = (a, 'Q')  # kmet se spremeni v kraljico  
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
        
        if d == 'P' and novo_polje[0] == 8 or novo_polje[0] == 1:
            self.postavitev[novo_polje] = (c, 'Q')  # kmet se spremeni v kraljico  
        else:
            self.postavitev[novo_polje] = (c, d)
        
        self.svoja_polja = {polje for polje in self.postavitev if self.postavitev[polje][0] == self.barva}
        self.nasprotnikova_polja = set(zasedena_polja.keys()).difference(self.svoja_polja)
        if zmaga(self.nasprotnikova_barva, zasedena_polja):
            return PORAZ
        if zmaga(self.barva, zasedena_polja):
            return ZMAGA

def nova_igra(barva, težavnost):
    nasprotnikova_barva = {'b', 'č'}.difference({barva}).pop()
    return igra(nasprotnikova_barva, težavnost)

import bottle
import model

sah = model.sah()
SECRET = 'sah'

bottle.TEMPLATE_PATH.insert(0, 'sah_views')

@bottle.get('/')
def osnovna_stran():
    return bottle.template('prva_stran.tpl')

@bottle.get('/sah_img/<picture>')
def static_file(picture):
    return bottle.static_file(picture, 'sah_img')

@bottle.post('/nova_igra/')
def nova_igra():
    barva = bottle.request.forms.getunicode('barva')
    težavnost = int(bottle.request.forms.getunicode('tezavnost'))
    id_igre = sah.nova_igra(barva, težavnost)
    bottle.response.set_cookie('id_igre', id_igre, path='/', secret=SECRET)
    print(id_igre)
    bottle.redirect('/igra/')

@bottle.get('/igra/')
def pokaži_igro():
    id_igre = bottle.request.get_cookie('id_igre', secret=SECRET)
    igra, stanje = sah.igre[id_igre]
    print(sah.igre)
    print(igra, stanje, id_igre)
    return bottle.template('igra.tpl', igra=igra, stanje=stanje, id_igre=id_igre, zmaga=model.ZMAGA, poraz=model.PORAZ)

slovar = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8}

def vnos_v_nabor(vnos):   # vnos je oblike '2, c'
    sez = []
    if vnos[0].isnumeric():
        sez.append(int(vnos[0]))
        if vnos[3] in 'abcdefgh':
            sez.append(slovar[vnos[3].lower()])
            if len(vnos) == 4:
                return tuple(sez)
    else:
        return None

@bottle.post('/poteza/')
def poteza():
    id_igre = bottle.request.get_cookie('id_igre', secret=SECRET)
    staro_polje = bottle.request.forms.getunicode('staro polje')
    novo_polje = bottle.request.forms.getunicode('novo polje')
    if staro_polje != None and novo_polje != None:
        if sah.poteza_igralca(id_igre, vnos_v_nabor(staro_polje), vnos_v_nabor(novo_polje)) != model.NAPAČNA_POTEZA:
            sah.poteza_računalnika(id_igre)
    bottle.redirect('/igra/')

bottle.run(debug=True, reloader=True)
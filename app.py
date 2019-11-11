from flask import Flask, jsonify, request
import json
import Scraping as scr
import Database as db

app = Flask(__name__)

listaLibros = [
    {
        'id': 1,
        'url': 'https://www.buscalibre.cl/libro-y-si-el-tiempo-no-existiera/9788425440571/p/51475704',
    },
    {
        'id': 2,
        'url': u'https://www.buscalibre.cl/libro-siete-breves-lecciones-de-fisica/9786078441433/p/47429624'
    }
]


@app.route('/apidatos', methods=['GET'])
def get_tasks():
    datos = []
    for dat in listaLibros:
        srapp = scr.scraping()
        srapp.url = dat['url']
        srapp.data()
        datos.append({
            'name': srapp.name,
            'price': srapp.price
        })
    return jsonify(datos)


@app.route('/almacenaLink', methods=['POST'])
def set_link():
    dtb = db.database()
    query = dtb.setLink()

    data = request.json
    return jsonify({
        'ok': 200,
        'data': data['test'],
        'numero': data['hola'],
        'respuestadb': query
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

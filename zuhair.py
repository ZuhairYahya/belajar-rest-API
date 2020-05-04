from flask import Flask, request
import json

app = Flask('zuhairyahya')

@app.route('/', methods=['GET'])
def index():
    data = {
        'message': 'DUnia Sedang Tidak Baik :)'
    }
    return json.dumps(data)

@app.route('/', methods=['POST'])
def index_post():
    data = request.get_json()
    berhasil = {
        'message': f'Selamat Datang {data["username"]}'
    }
    return json.dumps(berhasil)

app.run(debug=True)
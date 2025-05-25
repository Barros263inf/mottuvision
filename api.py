from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

CAMINHO_JSON = os.path.join(os.path.dirname(__file__), 'plates_beamsearch.json')

@app.route('/placas', methods=['GET'])
def listar_todas_as_placas():
    try:
        with open(CAMINHO_JSON, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

        if not dados:
            return jsonify({"erro": "JSON vazio"}), 400

        # Gera uma lista de objetos {"Placa": <placa>}
        placas = [{"Placa": placa} for placa in dados.keys()]

        return jsonify(placas), 200

    except Exception as e:
        return jsonify({"erro": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

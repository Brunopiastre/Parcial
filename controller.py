from flask import Flask, request, jsonify
from service import MutantService

app = Flask(__name__)
mutant_service = MutantService()  # Aquí se crea la instancia correctamente

@app.route('/mutant/', methods=['POST'])
def check_mutant():
    dna = request.json.get("dna", [])
    if mutant_service.is_mutant(dna):
        return jsonify({"message": "Mutant detected"}), 200
    else:
        return jsonify({"message": "Not a mutant"}), 403

@app.route('/stats', methods=['GET'])
def stats():
    stats = mutant_service.get_stats()
    return jsonify(stats)
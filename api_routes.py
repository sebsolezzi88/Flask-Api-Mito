import csv
from flask import Blueprint,jsonify
from funciones import normalice_text

api = Blueprint("api",__name__,url_prefix="/api/v1")

# Cargar al iniciar
with open('data/seres_mitologicos.csv', encoding='utf-8') as archivo:
    SERES = list(csv.DictReader(archivo))


@api.route("/all")
def all_data():
    return  jsonify(SERES),200

@api.route("/id/<id>")
def get_by_id(id:str):
    
    filter_data = [data for data in SERES if normalice_text(data['id'].lower()) == normalice_text(id)]
    return jsonify(filter_data),200

@api.route("/mitologia/<mythology>")
def get_by_mythology(mythology:str):

    filter_data = [data for data in SERES if normalice_text(data['Mitologia'].lower()) == normalice_text(mythology)]
    return jsonify(filter_data),200

@api.route("/tipo/<tipo>")
def get_by_type(tipo:str):

    filter_data = [data for data in SERES if normalice_text(data['Tipo'].lower()) == normalice_text(tipo)]
    return jsonify(filter_data),200

@api.route("/nombre/<name>")
def get_by_name(name:str):
    
    filter_data = [data for data in SERES if normalice_text(data['Nombre'].lower()) == normalice_text(name)]
    return jsonify(filter_data),200

@api.route("/origen/<origin>")
def get_by_origin(origin:str):
    
    filter_data = [data for data in SERES if normalice_text(data['Origen'].lower()) == normalice_text(origin)]
    return jsonify(filter_data),200

@api.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Ruta no encontrada"
    }), 404
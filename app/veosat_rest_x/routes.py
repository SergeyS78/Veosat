"""Module contains application routes"""

from flask import Blueprint, jsonify
from flask_restx import Resource
from app.database import db
from app.rest_x import api
from app.veosat.models import Vehiculo, Posiciones

rest_x = api.namespace('veosat_rest_x', description='veosat_rest_x operations')

@rest_x.route('/get_id_state/<int:id_state>')
class GetIdState(Resource):
    """Seleccionar los vehíclos con un parámetro para filtrar el id_estado
    Example of the route:
    http://127.0.0.1:5000/veosat_rest_x/get_id_state/1
    """

    def get(self, id_state):
        try:
            vehicles = db.session.query(Vehiculo.matricula).filter(
                Vehiculo.id_estado == id_state).all()

            print(vehicles)
            res = str(vehicles)
        except Exception as err:
            res = str(err)

        return jsonify(res)

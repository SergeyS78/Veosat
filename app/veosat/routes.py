"""Module contains application routes"""

from flask import Blueprint, jsonify
from app.database import db
from app.veosat.models import Vehiculo, Posiciones

module = Blueprint('veosat', __name__, url_prefix='/veosat')


@module.route('/db_init/')
def db_init():
    """Create a data base tables".
    Example of the route:
    http://127.0.0.1:5000/veosat/db_init/
    """

    try:
        db.drop_all()
        db.create_all()

        veh_1 = Vehiculo(matricula='1234ABC')
        veh_2 = Vehiculo(matricula='5678DEF')
        db.session.add_all([veh_1, veh_2])
        db.session.commit()

        pos_1 = Posiciones(latitud=52, longitud=63, velocidad=20, vehiculo=veh_1)
        pos_2 = Posiciones(latitud=52, longitud=63, velocidad=10, vehiculo=veh_2)
        db.session.add_all([pos_1, pos_2])
        db.session.commit()

        res = {'status': 'ok'}
    except Exception as err:
        res = str(err)

    return jsonify(res)


@module.route('/check_velocity/')
def check_velocity():
    """Check vehicle velocity status".
    Example of the route:
    http://127.0.0.1:5000/veosat/check_velocity/
    """

    try:
        p_list = db.session.query(Posiciones).filter(Posiciones.velocidad > 10).all()

        for position in p_list:
            position.vehiculo.id_estado = 1
            db.session.add(position)
            db.session.commit()

        vehicles = db.session.query(Vehiculo.id_estado).all()
        res = str(vehicles)
    except Exception as err:
        res = str(err)

    return jsonify(res)


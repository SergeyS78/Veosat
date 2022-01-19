"""Database Models"""

from app.database import db


class Vehiculo(db.Model):
    """Vehiculo data base model"""
    id = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.String(10))
    id_estado = db.Column(db.Integer)
    posiciones = db.relationship('Posiciones', backref='vehiculo', lazy='dynamic')

    def __repr__(self):
        """__repr__ method tells Python how to print objects of this class.
        >>> v = Vehiculo(matricula='1234ABC')
        >>> v
        <Vehiculo 1234ABC>
        """
        return '<Vehiculo {}>'.format(self.matricula)


class Posiciones(db.Model):
    """Vehiculo data base model"""
    id = db.Column(db.Integer, primary_key=True)
    latitud = db.Column(db.Float)
    longitud = db.Column(db.Float)
    velocidad = db.Column(db.Float)
    id_vehiculo = db.Column(db.Integer, db.ForeignKey('vehiculo.id'))

    def __repr__(self):
        """__repr__ method tells Python how to print objects of this class.
        >>> p = Posiciones(latitud=52, longitud=63)
        >>> p
        <Posiciones (latitud=52, longitud=63)>
        """
        return '<Posiciones {}>'.format(
            "(latitud=" + str(self.latitud) + ", longitud=" + str(self.longitud) + ")")

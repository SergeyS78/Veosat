"""Data base application. One connection pool for all Flask instances"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from flask import Flask

app = Flask(__name__)

from app import routes
from app.class_x import x_routes
from app.class_ix import ix_routes
from app.class_x.bio import bio_routes
from app.class_x.chem import chem_routes
from app.class_x.maths import maths_routes
from app.class_x.phys import phys_routes
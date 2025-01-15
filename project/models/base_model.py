import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from peewee import *
from datetime import date
from config import db

class BaseModel(Model):
    class Meta:
        database = db


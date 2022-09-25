from django.db import models
import datetime
from pony.orm import *

db = Database()

# Create your models here.
class Media(db.Entity):
    uid = Required(str)
    type = Required(str)
    media_filename = Required(str)
    upload_timestamp = Required(datetime.datetime, precision=6)

sql_debug(True)
db.bind(provider='mysql', host='127.0.0.1', user='root', passwd='password', db='museum_practice')
db.generate_mapping(create_tables=True)
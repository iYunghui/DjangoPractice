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

host_name = ""
user_name = ""
password = ""
db_name = ""
with open('../museum.cnf') as f:
    for line in f.readlines():
        string = line.split()
        if string[0] == 'DATABASE':
            db_name = string[2].replace("\"", "")
        elif string[0] == 'USER':
            user_name = string[2].replace("\"", "")
        elif string[0] == 'PASSWORD':
            password = string[2].replace("\"", "")
        elif string[0] == 'HOST':
            host_name = string[2].replace("\"", "")

db.bind(provider='mysql', host=host_name, user=user_name, passwd=password, db=db_name)
db.generate_mapping(create_tables=True)
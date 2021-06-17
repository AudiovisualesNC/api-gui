from .connection import DatabaseClass
import os
import sys
import json
import warnings
from datetime import datetime

#############################
#     USO EN DESARROLLO     #
#############################

#os.environ['MYSQL_HOST'] = "192.168.3.250"
#os.environ['MYSQL_USER'] = "user"
#os.environ['MYSQL_PASS'] = "password"
#os.environ['MYSQL_DB'] = "db"

###################################

host = os.environ['MYSQL_HOST']
user = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PASS']
db_name = os.environ['MYSQL_DB']
# Import base de datos
db = DatabaseClass(host=host, user=user, password=password, db=db_name)


def get_all_rooms():
    """
    :username: str
    :return: pc: {dict1} # Hostname es unico por tanto solo puede haber un registro con ese hostname
    """
    try:
        db.connect()
        my_cursor = db.mysqldb.cursor(dictionary=True)
        my_cursor.execute("SELECT * FROM db.INVENTORY")
        return my_cursor.fetchall()

    except:
        print("Error get_all_rooms")

    finally:
        db.disconnect()

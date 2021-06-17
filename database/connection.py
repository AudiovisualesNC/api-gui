#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mysql.connector import Error
import sys
import mysql.connector


class DatabaseClass:
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    def connect(self):
        try:
            self.mysqldb = mysql.connector.connect(host=self.host, user=self.user, password=self.password,
                                                   database=self.db)
        except Error as e:
            sys.stderr.write(str(e))

    def disconnect(self):
        try:
            self.mysqldb.close()
        except Error as e:
            sys.stderr.write(str(e))
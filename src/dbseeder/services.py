#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
services
----------------------------------
The basic services
'''

import datetime
import ceODBC as odbc
from dateutil.parser import parse


class Caster(object):

    """takes argis row input and casts it to the defined schema type"""
    @staticmethod
    def cast(value, cast_to):
        if value is None:
            return None

        try:
            value = value.strip()
        except:
            pass

        if cast_to == 'string':
            cast = str
        elif cast_to == 'int':
            cast = int
        elif (cast_to == 'float' or
              cast_to == 'double'):
            cast = float
        elif cast_to == 'date':
            if isinstance(value, datetime.datetime):
                cast = lambda x: x
            elif value == '':
                return None
            else:
                cast = parse
        elif cast_to == 'bool':
            cast = lambda x: x.lower() in ('yes', 'true', 't', '1')
        elif cast_to == 'bit':
            cast = Caster._cast_bit
        else:
            raise Exception(cast_to, 'No casting method created.')

        try:
            value = cast(value)

            if value == '':
                return None

            return value
        except:
            return None

    @staticmethod
    def _cast_bit(value):
        if value.lower() == 'y':
            return 1
        return 0


class BrickLayer(object):

    """inserts the records into the database"""

    def __init__(self, connection_string=None):
        super(BrickLayer, self).__init__()

        self.batch_size = 10000
        self.insert_statements = {
            'crash': 'INSERT INTO Crash VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            'rollup': 'INSERT INTO Rollup VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            'driver': 'INSERT INTO Driver VALUES (?, ?, ?, ?, ?, ?, ?)'
        }
        self.connection_string = connection_string

        if not self.connection_string:
            self.connection_string = (
                r'Driver={SQL Server};' +
                r'Server=(local)\SQLEXPRESS;' +
                r'Database=crash;' +
                r'Trusted_Connection=Yes;'
            )

    def insert_rows(self, table_name, rows):
        if table_name.lower() not in self.insert_statements.keys():
            raise Exception(table_name, 'Do not know how to insert this type of record')

        connection = odbc.connect(self.connection_string)
        cursor = connection.cursor()

        command = self.insert_statements[table_name.lower()]

        i = 1
        start = 0
        end = self.batch_size
        try:
            print 'total rows to insert {}'.format(len(rows))

            while start < len(rows):
                batched_rows = rows[start:end]

                cursor.executemany(command, batched_rows)
                connection.commit()

                i = i + 1
                start = end
                end = i * self.batch_size + 1
        except:
            # import pprint
            # pp = pprint.PrettyPrinter(indent=4)
            # pp.pprint(batched_rows)

            print '{} {}-{}'.format(table_name, start, end)

            from nose.tools import set_trace
            set_trace()

            raise
        finally:
            cursor.close()
            connection.close()

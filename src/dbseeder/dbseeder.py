#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
dbseeder
----------------------------------
the dbseeder module
'''

from os.path import basename, splitext
import timeit
import glob
import csv
from models import Schema, Lookup
from services import Caster


class DbSeeder(object):
    def __init__(self):
        super(DbSeeder, self).__init__()

    def process(self, location):
        files = glob.glob(location + '*.csv')

        for file in files:
            start = timeit.default_timer()

            with open(file) as csv_file:
                reader = csv.DictReader(csv_file)

                for row in reader:
                    self._etl_row(file, row)

            end = timeit.default_timer()
            print '{}: {}'.format(file, end-start)

    def _etl_row(self, file, row):
        file_name = splitext(basename(file))[0]
        func = None

        if 'crash' in file_name:
            func = self._etl_crash
        elif 'drivers' in file_name:
            func = self._etl_driver
        elif 'rollup' in file_name:
            func = self._etl_rollup
        else:
            raise Exception(file, 'Not a part of the crash, drivers, rollops convention')

        return func(row)

    def _etl_crash(self, row):
        input_keys = Schema.rollup.keys()
        etl_keys = map(lambda x: x['map'], Schema.rollup.values())

        etl_row = dict.fromkeys(etl_keys)

        for key in row.keys():
            if key not in input_keys:
                continue

            etl_info = Schema.rollup[key]

            value = row[key]
            etl_value = Caster.cast(value, etl_info['type'])
            etl_row[etl_info['map']] = etl_value

        return etl_row

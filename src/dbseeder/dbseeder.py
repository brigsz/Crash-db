#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
dbseeder
----------------------------------
the dbseeder module
'''

from os.path import basename, splitext, join
import timeit
import glob
import csv
from models import Schema, Lookup
from services import Caster


class DbSeeder(object):

    def __init__(self):
        super(DbSeeder, self).__init__()

    def process(self, location):
        files = self._get_files(location)

        for file in files:
            start = timeit.default_timer()

            with open(file) as csv_file:
                reader = csv.DictReader(csv_file)

                for row in reader:
                    self._etl_row(file, row)

            end = timeit.default_timer()
            print '{}: {}'.format(file, end - start)

    def _get_files(self, location):
        if not location:
            raise Exception('Pass in a location containing csv files to import.')

        files = glob.glob(join(location, '*.csv'))

        if len(files) < 1:
            raise Exception(location, 'No csv files found.')

        return files

    def _etl_row(self, file, row):
        file_name = splitext(basename(file))[0]

        if 'crash' in file_name:
            input_keys = Schema.crash_input_keys
            etl_keys = Schema.crash_etl_keys
            lookup = Schema.crash
        elif 'driver' in file_name:
            input_keys = Schema.driver_input_keys
            etl_keys = Schema.driver_etl_keys
            lookup = Schema.driver
        elif 'rollup' in file_name:
            input_keys = Schema.rollup_input_keys
            etl_keys = Schema.rollup_etl_keys
            lookup = Schema.rollup
        else:
            raise Exception(file, 'Not a part of the crash, drivers, rollops convention')

        return self._etl_row_generic(row, lookup, input_keys, etl_keys)

    def _etl_row_generic(self, row, lookup, input_keys, etl_keys):
        etl_row = dict.fromkeys(etl_keys)

        for key in row.keys():
            if key not in input_keys:
                continue

            etl_info = lookup[key]

            value = row[key]
            etl_value = Caster.cast(value, etl_info['type'])

            if 'lookup' in etl_info.keys():
                lookup_name = etl_info['lookup']
                values = Lookup.__dict__[lookup_name]

                if etl_value in values.keys():
                    etl_value = values[etl_value]

            etl_row[etl_info['map']] = etl_value

        return etl_row

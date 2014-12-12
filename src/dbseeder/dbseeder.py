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
from services import Caster, BrickLayer


class DbSeeder(object):

    def __init__(self):
        super(DbSeeder, self).__init__()
        self.brick_layer = BrickLayer()

    def process(self, location):
        files = self._get_files(location)

        for file in files:
            file_name = splitext(basename(file))[0]
            start = timeit.default_timer()
            items = []

            with open(file) as csv_file:
                reader = csv.DictReader(csv_file)

                for row in reader:
                    items.append(self._etl_row(file_name, row))

            self.brick_layer.insert_rows(file_name, items)
            items = []

            end = timeit.default_timer()
            print '{}: {}'.format(file, end - start)

    def _get_files(self, location):
        if not location:
            raise Exception('Pass in a location containing csv files to import.')

        files = glob.glob(join(location, '*.csv'))

        if len(files) < 1:
            raise Exception(location, 'No csv files found.')

        return files

    def _etl_row(self, file_name, row):
        if 'crash' in file_name:
            input_keys = Schema.crash_input_keys
            etl_keys = Schema.crash_etl_keys
            lookup = Schema.crash
            formatter = Schema.crash_schema_ordering
        elif 'driver' in file_name:
            input_keys = Schema.driver_input_keys
            etl_keys = Schema.driver_etl_keys
            lookup = Schema.driver
            formatter = Schema.driver_schema_ordering
        elif 'rollup' in file_name:
            input_keys = Schema.rollup_input_keys
            etl_keys = Schema.rollup_etl_keys
            lookup = Schema.rollup
            formatter = Schema.rollup_schema_ordering
        else:
            raise Exception(file, 'Not a part of the crash, drivers, rollops convention')

        return self._etl_row_generic(row, lookup, input_keys, etl_keys, formatter)

    def _etl_row_generic(self, row, lookup, input_keys, etl_keys, formatter=None):
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

        if formatter:
            return formatter(etl_row)

        return etl_row

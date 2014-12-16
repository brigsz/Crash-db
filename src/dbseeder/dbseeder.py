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
            print 'processing {}'.format(file)

            file_name = splitext(basename(file))[0]
            table_name = self._get_table_name(file_name)
            start = timeit.default_timer()
            items = []

            with open(file, 'r') as csv_file:
                reader = csv.DictReader(csv_file)

                for row in reader:
                    items.append(self._etl_row(table_name, row))

            self.brick_layer.insert_rows(table_name, items)
            items = []

            end = timeit.default_timer()
            print 'processing time: {}'.format(end - start)

    def get_lengths(self, location):
        files = self._get_files(location)
        items = {
            'crash': {}
        }

        for file in files:
            file_name = splitext(basename(file))[0]
            table_name = self._get_table_name(file_name)

            with open(file, 'r') as csv_file:
                reader = csv.DictReader(csv_file)

                if table_name == 'crash':
                    lookup = Schema.crash
                else:
                    continue

                try:
                    for row in reader:
                        for key in row.keys():
                            if key not in lookup.keys():
                                continue
                            if lookup[key]['type'] != 'string':
                                continue

                            if items[table_name].setdefault(key, 0) >= len(row[key]):
                                continue

                            items[table_name][key] = len(row[key])
                except:
                    print file
                    raise

        import pprint
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(items)

    def _get_files(self, location):
        if not location:
            raise Exception('Pass in a location containing csv files to import.')

        files = glob.glob(join(location, '*.csv'))

        if len(files) < 1:
            raise Exception(location, 'No csv files found.')

        return files

    def _etl_row(self, table_name, row):
        if table_name == 'crash':
            input_keys = Schema.crash_input_keys
            etl_keys = Schema.crash_etl_keys
            lookup = Schema.crash
            formatter = Schema.crash_schema_ordering
        elif table_name == 'driver':
            input_keys = Schema.driver_input_keys
            etl_keys = Schema.driver_etl_keys
            lookup = Schema.driver
            formatter = Schema.driver_schema_ordering
        elif table_name == 'rollup':
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

    def _get_table_name(self, file_name):
        if 'crash' in file_name:
            return 'crash'
        elif 'driver' in file_name:
            return 'driver'
        elif 'rollup' in file_name:
            return 'rollup'
        else:
            return None

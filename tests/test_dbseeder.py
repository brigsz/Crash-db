#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
dbseeder
----------------------------------
test the dbseeder module
'''

import unittest
import datetime
from dbseeder.dbseeder import DbSeeder


class TestDbSeeder(unittest.TestCase):

    def test_etl_crash(self):
        patient = DbSeeder()
        row = {
            'BICYCLIST_INVOLVED': 'N',
            'COMMERCIAL_MOTOR_VEH_INVOLVED': 'Y',
            'CRASH_DATETIME': '2011-01-24 15:00:00',
            'CRASH_ID': '10380000',
            'DOMESTIC_ANIMAL_RELATED': 'N',
            'DUI': 'N',
            'IMPROPER_RESTRAINT': 'N',
            'INTERSECTION_RELATED': 'N',
            'MOTORCYCLE_INVOLVED': 'N',
            'NIGHT_DARK_CONDITION': 'N',
            'OLDER_DRIVER_INVOLVED': 'N',
            'OVERTURN_ROLLOVER': 'N',
            'PEDESTRIAN_INVOLVED': 'N',
            'TEENAGE_DRIVER_INVOLVED': 'N',
            'WILD_ANIMAL_RELATED': 'N'
        }
        expected = {
            'bicycle': 0,
            'commercial_vehicle': 1,
            'date': datetime.datetime(2011, 1, 24, 15, 0, 0),
            'id': 10380000,
            'animal_domestic': 0,
            'dui': 0,
            'improper_restraint': 0,
            'intersection': 0,
            'motorcycle': 0,
            'dark': 0,
            'elder': 0,
            'rollover': 0,
            'pedestrian': 0,
            'teenager': 0,
            'animal_wild': 0
         }

        self.maxDiff = None
        actual = patient._etl_crash(row)
        self.assertEqual(actual, expected)

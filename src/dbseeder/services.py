#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
services
----------------------------------
The basic services
'''

import datetime
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

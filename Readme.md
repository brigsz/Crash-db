[![Build Status](https://travis-ci.org/agrc/Crash-db.svg?branch=travis)](https://travis-ci.org/agrc/Crash-db)

Crash DB
========

A db seeder etl tool for crash data.

### Usage
`python -m dbseeder path/to/csv's`

### Tests
`tox`

### Problems
`expecting string data` means the lookup value was not in the models table. Change batch size to 2 and look for a number where there should be a value. Add the number: None

`string or binary data to be truncated` - run `python -m dbseeder path/to/csv's --length` and adjust sql schema 
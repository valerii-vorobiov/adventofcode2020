import re
from cerberus import Validator


def validate_height(field, value, error):
    msg = ('height is not valid.'
           ' If cm, the number must be at least 150 and at most 193. '
           'If in, the number must be at least 59 and at most 76.')
    if value.endswith('cm'):
        try:
            h = int(value.replace('cm', ''))
            if not 150 <= h <= 193:
                error(field, msg)
        except Exception:
            error(field, msg)
    elif value.endswith('in'):
        try:
            h = int(value.replace('in', ''))
            if not 59 <= h <= 76:
                error(field, msg)
        except Exception:
            error(field, msg)
    else:
        error(field, msg)


class Passport:
    schema = {'byr': {'type': 'integer',
                      'min': 1920,
                      'max': 2002,
                      'coerce': int},
              'iyr': {'type': 'integer',
                      'min': 2010,
                      'max': 2020,
                      'coerce': int},
              'eyr': {'type': 'integer',
                      'min': 2020,
                      'max': 2030,
                      'coerce': int},
              'hgt': {'check_with': validate_height},
              'hcl': {'type': 'string',
                      'regex': '#[0-9abcdef]{6}'},
              'ecl': {'type': 'string',
                      'allowed': ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']},
              'pid': {'type': 'string',
                      'regex': '[0-9]{9}'}}
    required = set(schema.keys())

    def __init__(self, fields):
        self.fields = fields

    def is_valid_fields(self):
        return not bool(self.required - self.fields.keys())

    def is_valid_values(self):
        if not self.is_valid_fields():
            return False
        v = Validator(self.schema, purge_unknown=True)
        v.allow_unknown = True
        return v.validate(self.fields)


def read_input():
    with open('input') as f:
        lines = re.split(r'\n\n', f.read(), flags=re.MULTILINE)
    passports = [split_fields(l) for l in lines]
    return [make_dict(p) for p in passports]


def make_dict(p):
    return dict(tuple(item.split(':')) for item in p)


def split_fields(passport):
    return passport.replace('\n', ' ').split(' ')


def main1():
    lines = read_input()
    return sum(Passport(fields).is_valid_fields() for fields in lines)


def main2():
    lines = read_input()
    return sum(Passport(fields).is_valid_values() for fields in lines)
    # for fields in lines:
    #     print(fields)
    #     print(Passport(fields).is_valid_values())


def main(task):
    return {1: main1, 2: main2}[task]()


if __name__ == '__main__':
    print(main(2))

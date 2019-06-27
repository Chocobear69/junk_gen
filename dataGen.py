import random
from datetime import datetime
from copy import deepcopy

from config import config

bin = config.data_types['bin']
num = config.data_types['num']
char = config.data_types['char']
dttm = config.data_types['datetime']

alphabet = config.english_alphabet


def char_gen(length: int):
    """
    Generate random meaningless string type data
    :param length: int string length
    :return: string
    """
    result = ''
    if length < 0:
        length = random.randrange(1, 5)
    for i in range(0, length):
        result += random.choice(alphabet)
    return result


def num_gen():
    """
    Generate random int type data from one to thousand
    :return: int
    """
    return random.randint(0, 1000)


def bin_gen():
    """
    Generate random int type binary data - one or zero
    :return: int
    """
    return random.randrange(2)


def dttm_gen():
    """
    Genarate random datetime object from 1900 year to 2019 year
    :return: datetime
    """
    year = random.randrange(1900, 2020)
    month = random.randrange(1, 13)
    day = random.randrange(1, 29) if month == 2 else random.randrange(1, 31)
    hour = random.randrange(1, 24)
    minute = random.randrange(1, 60)
    second = random.randrange(1, 60)

    result = datetime(year, month, day, hour, minute, second).strftime('%Y-%m-%d %H:%M:%S')

    return str(result)


def arg_parse():
    """
    Parse input data to list
    :return: dict
    """
    print('Attribute types?')
    val_types = [i for i in input().split()]
    print('Char length ?')
    char_lenghts = [int(i) for i in input().split()]
    print('Records number?')
    records_num = int(input())
    if val_types and records_num:
        result = {
            'TYPES': val_types,
            'CHAR_LENGTHS': char_lenghts,
            'RECORD_NUMBER': records_num
        }
        return result
    raise ValueError('Not enougth arguments!')


def generator(dt_list, len_list):
    """
    Generate data using functions above due to data type
    :param dt_list: list with data types
    :param len_list: list with lengths
    :return: list with
    """
    result = []
    length = len_list
    for i in dt_list:
        if i in bin:
            result.append(bin_gen())
        elif i in num:
            result.append(num_gen())
        elif i in char:
            result.append(char_gen(length[0]))
            length.pop(0)
        elif i in dttm:
            result.append(dttm_gen())
        else:
            result.append('TROUBLE')
    return result


def query_generator(strings):
    values = ''
    for i in strings:
        values += str(i)
        values += ',' if strings.index(i) < len(strings)-1 else ';'
    values = values.replace('[', '(').replace(']', ')')
    return values


def looper(args):
    result = []
    rng = range(0, args['RECORD_NUMBER'])
    for i in rng:
        result.append(generator(args['TYPES'], deepcopy(args['CHAR_LENGTHS'])))
    return result


def main():
    arguments = arg_parse()
    values = looper(arguments)
    query = query_generator(values)
    print(query)


if __name__ == '__main__':
    main()

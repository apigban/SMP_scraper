#!/usr/bin/env python3.7
import os
import codecs

file_list = []

file_dump_path = '/home/apigban/PycharmProjects/SMP_scraper/Downloader/dump'


def file_walker():
    for root, dirs, files in os.walk('/home/apigban/PycharmProjects/SMP_scraper/Downloader/dump'):
        for filename in files:
            file_list.append(filename)
    return file_list


def csv_validator(csv_file_list):
    """
    Checks if csv_file in csv_file_list can be opened using utf-8 encoding.
    A file that passed the check will have a "VALID" tag written to invalid.txt
    A file that is encoded differently from utf-8 (did not pass) will have
    an "INVALID" tag.
    :param csv_file_list:
    """
    for csv_file in csv_file_list:

        try:
            file = codecs.open(f'{file_dump_path}/{csv_file}', encoding='utf-8', errors='strict')
            for line in file:
                pass
            with open(f'/home/apigban/PycharmProjects/SMP_scraper/Parser/log/valid.txt', 'a') as open_file:
                open_file.write(f'{csv_file}\n')

        except UnicodeDecodeError:
            with open(f'/home/apigban/PycharmProjects/SMP_scraper/Parser/log/invalid.txt', 'a') as open_file:
                open_file.write(f'{csv_file}\n')


csv_list = file_walker()
csv_validator(csv_list)

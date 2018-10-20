#!/usr/bin/env python3.7
import os
import codecs

file_dump_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Downloader/dump/'))
file_list = []


def file_walker(dump_path):
    for root, dirs, files in os.walk(file_dump_path):
        for filename in files:
            file_list.append(filename)
    return file_list


def csv_validator():
    """
    Checks if csv_file in csv_file_list can be opened using utf-8 encoding.
    A file that passed the check will have a "VALID" tag written to invalid.txt
    A file that is encoded differently from utf-8 (did not pass) will have
    an "INVALID" tag.
    :param csv_file_list:
    """

    csv_file_list = file_walker(file_dump_path)

    valid_file_list = []
    invalid_file_list = []
    for csv_file in csv_file_list:
        try:
            file = codecs.open(f'{file_dump_path}/{csv_file}', encoding='utf-8', errors='strict')
            for line in file:
                pass
            # with open(f'/home/apigban/PycharmProjects/SMP_scraper/Parser/log/valid.txt', 'a') as open_file:
            #    open_file.write(f'{csv_file}\n')
            valid_file_list.append(csv_file)
        except UnicodeDecodeError:
            # with open(f'/home/apigban/PycharmProjects/SMP_scraper/Parser/log/invalid.txt', 'a') as open_file:
            #    open_file.write(f'{csv_file}\n')
            invalid_file_list.append(csv_file)

    return valid_file_list, invalid_file_list


if __name__ == '__main__':
    csv_validator()

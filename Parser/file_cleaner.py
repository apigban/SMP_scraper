import csv
import os
import re

import Log.log as log


def get_invalid_file():
    """
    Opens INvalid_file_log, converts the file to a csv.reader object and
    reads all items from the object.
    :return:
    """
    invalid_files_list = []

    with open(invalid_file_log) as csv_file:
        all_rows_obj = csv.reader(csv_file)
        for row in all_rows_obj:
            invalid_files_list.append(row[0])

    return invalid_files_list


def get_Valid_file():
    """
    Opens valid_file_log, converts the file to a csv.reader object and
    reads all items from the object. Returns a valid_files_list.
    :return:
    """
    valid_files_list = []

    with open(valid_file_log) as csv_file:
        all_rows_obj = csv.reader(csv_file)
        for row in all_rows_obj:
            valid_files_list.append(row[0])

    return valid_files_list


def delete_invalid_file(invalid_files_list):
    """
    Iterates through invalid_files_list to remove invalid files from data_path
    If a file is not found, log the exception and continue iteration
    :return: None
    """
    for invalid_file in invalid_files_list:
        try:
            os.remove(f'{data_path}{invalid_file}')
            file_cleaner_log.info(f'{invalid_file} removed')
        except FileNotFoundError as FNFError:
            file_cleaner_log.error(f'{invalid_file} not found. Error: {FNFError}')
            pass


def preproc_valid_files(files_for_preproc):
    valid_file_counter = None
    invalid_file_counter = None

    pre_processing_list = []

    for valid_csv_file in files_for_processsing:
        with open(f'{data_path}{valid_csv_file}') as csv_file:
            all_row_obj = next(csv.reader(csv_file))

            for row in all_row_obj:
                match = re.match(string_pattern, str(row))
                if match is None:
                    file_cleaner_log.info(f'{valid_csv_file} contains non-financial data')
                else:
                    file_cleaner_log.info(f'{valid_csv_file} is a valid csv file')
                    pre_processing_list.append(f'{valid_csv_file}')
    return pre_processing_list


if __name__ == '__main__':
    # Initialize Logger
    file_cleaner_log = log.get_logger(__name__)

    # Present Data Dump Path
    data_path = '/home/apigban/PycharmProjects/SMP_scraper/Downloader/dump/'

    # Deletion Process for files that DIDN'T PASS the utf-8 encoding check
    invalid_file_log = '/home/apigban/PycharmProjects/SMP_scraper/Parser/log/invalid.txt'
    files_for_deletion = get_invalid_file()
    delete_invalid_file(files_for_deletion)

    # Pre-process for files that PASSED the utf-8 encoding check
    valid_file_log = '/home/apigban/PycharmProjects/SMP_scraper/Parser/log/valid.txt'
    files_for_processsing = get_Valid_file()

    string_pattern = "\A\^FINANCIAL"

    preproc_valid_files(files_for_processsing)

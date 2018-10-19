import os
import csv
import Log.log as log

file_cleaner_log = log.get_logger(__name__)

data_path = '/home/apigban/PycharmProjects/SMP_scraper/Downloader/dump/'

target_file = '/home/apigban/PycharmProjects/SMP_scraper/Parser/log/invalid.txt'


def file_walker():
    for root, dirs, files in os.walk('/home/apigban/PycharmProjects/SMP_scraper/Downloader/dump'):
        for filename in files:
            file_list.append(filename)
    return file_list


def get_invalid_file():
    invalid_files = []

    with open(target_file) as csv_file:
        all_rows_obj = csv.reader(csv_file)
        for row in all_rows_obj:
            invalid_files.append(row[0])

    return invalid_files


def delete_invalid_file(invalid_files_list):
    for invalid_file in invalid_files_list:
        os.remove(f'{data_path}{invalid_file}')
        file_cleaner_log.info(f'{invalid_file} removed')


files_for_deletion = get_invalid_file()

delete_invalid_file(files_for_deletion)

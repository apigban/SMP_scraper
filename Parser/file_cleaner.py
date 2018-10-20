import csv
import os
import re
import Log.log as log

### Validation steps:
#   1. Load row
#   2. if pattern is not found:     log to file
#   3. if pattern is found:         append filename to pre_processed_list
#   4. return pre_processed_list


# Initialize Logger
file_cleaner_log = log.get_logger(__name__)

# Present Data Dump Path
data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Downloader/dump/'))

# Deletion Process for files that DIDN'T PASS the utf-8 encoding check
invalid_file_log = os.path.dirname(__file__) + '/log/invalid.txt'
# files_for_deletion = get_invalid_file()
# delete_invalid_file(files_for_deletion)

valid_file_log = os.path.dirname(__file__) + '/log/valid.txt'
string_pattern = "\A\^FINANCIAL"

def delete_invalid_file(invalid_files_list):
    """
    Iterates through invalid_files_list to remove invalid files from data_path
    If a file is not found, log the exception and continue iteration
    :return: None
    """
    for invalid_file in invalid_files_list:
        try:
            os.remove(f'{data_path}/{invalid_file}')
            file_cleaner_log.info(f'{invalid_file} removed')
        except FileNotFoundError as FNFError:
            file_cleaner_log.error(f'{invalid_file} not found. Error: {FNFError}')
            pass


def preproc_valid_files(files_for_processing, valid_file_log_length):
    """
    On all files in dump_path, read first row
    if first row doesn't match ^FINANACIAL log to file
    else (means matched) append to pre_processed_list
    return pre_processed_list
    :param files_for_processing:
    :param valid_file_log_length:
    :return:
    """
    valid_file_counter = 0
    invalid_file_counter = None

    pre_processed_list = []

    for valid_csv_file in files_for_processing:
        with open(f'{data_path}/{valid_csv_file}') as csv_file:
            all_row_obj = next(csv.reader(csv_file))
            for row in all_row_obj:
                match = re.match(string_pattern, str(row))

                if match is None:
                    file_cleaner_log.info(f'{valid_csv_file} contains non-financial data')

                else:
                    file_cleaner_log.info(f'{valid_csv_file} is a valid csv file')
                    valid_file_counter += 1
                    pre_processed_list.append(f'{valid_csv_file}')

    file_cleaner_log.info(
        f'{valid_file_counter} pre-processed files. Files are checked if utf-8 encoded and starts with ^FINANCIAL.')
    file_cleaner_log.info(f'{valid_file_log_length - valid_file_counter} failed to pass pre-processing checks.')

    return pre_processed_list


if __name__ == '__main__':
    # Initialize Logger
    file_cleaner_log = log.get_logger(__name__)

    # Present Data Dump Path
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Downloader/dump/'))

    # Deletion Process for files that DIDN'T PASS the utf-8 encoding check
    invalid_file_log = os.path.dirname(__file__) + '/log/invalid.txt'

    # Validation for files that PASSED the utf-8 encoding check
    valid_file_log = os.path.dirname(__file__) + '/log/valid.txt'
    string_pattern = "\A\^FINANCIAL"

    #print(all_files_from_dump)

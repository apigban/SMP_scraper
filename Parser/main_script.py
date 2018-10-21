from Log import log
from Parser import utf8_validator, file_cleaner, file_parser
# This module calls multiple modules from the Parser directory.

#   Initialize Logger
pre_processor_log = log.get_logger(__name__)

#   Get Valid and Invalid file lists
valid_file_list, invalid_file_list = utf8_validator.csv_validator()

#   Pass invalid file list to deletion function in file_cleaner module
file_cleaner.delete_invalid_file(invalid_file_list)

#   Pass valid file list to deletion function in file_cleaner module
pre_processed_list = file_cleaner.preproc_valid_files(valid_file_list, len(valid_file_list))

#   Delete files from dump that doesn't start with ^FINANCIAL
for_removal = list(set(valid_file_list).difference(set(pre_processed_list)))
file_cleaner.delete_invalid_file(for_removal)

#   Sort and write rows to appropriate table in DB
file_parser.data_sorter(pre_processed_list)

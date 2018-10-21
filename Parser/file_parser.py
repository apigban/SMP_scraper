import re, csv
from Parser import utf8_validator
import Log.log as log

data_path = utf8_validator.file_dump_path

def regexer(row):
    """
    Matches financial sector data like "^FINANCIAL" and "^PSEI" with data in row,
    for a successful match function returns 'sector'.
    If row is stock data, meaning no match, like "\nAUB" or "\nTEL"return string(stock)
    :param row:
    :return:
    """
    sector_pattern = r'\^\w+'
    stock_pattern = r'\n\w+'

    #   match for sector, Sector examples: ^FINANCIAL ^HOLDING ^INDUSTRIAL
    sector_match = re.match(sector_pattern, row[0])

    #    match for stock, Stock examples: \nAUB \nTEL
    stock_match = re.match(stock_pattern, row[0])

    if bool(sector_match) is True:
        return 'sector'
    return 'stock'


# Call db_writer function
def data_sorter(pre_processed_list):
    """
    Opens a csv file passed by the main_script.py, Calls regexer() to identify if a
    row is Sector or Stock data.
    If regexer returns 'sector', writes row to sector db
    If regexer returns 'stock', writes row to stock db
    :param row:
    :return:
    """
    for file in pre_processed_list:

        sector_counter = 0
        stock_counter = 0

        with open(f'{data_path}/{file}') as raw_csv_record:
            all_rows = csv.reader(raw_csv_record)
            parser_log.info(f'Parsing file {file}.')
            for row in all_rows:
                if regexer(row) == 'sector':
                    #   Call Sector Class from models.py module
                    #   Populate Instance Variables
                    sector_counter += 1
                    parser_log.info(f'Sector {row[0]} data found on {file}')
                else:
                    # Call Stock Class from models.py module
                    # Populate Instance Variables
                    stock_counter += 1
                    parser_log.info(f'Stock {row[0]} data found on {file}')
            parser_log.info(f'{file} parsed successfully.')
            parser_log.info(f'STATISTICS for {file} : {sector_counter} sector data. {stock_counter} stock data.')


parser_log = log.get_logger(__name__)
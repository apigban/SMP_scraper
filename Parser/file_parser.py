import csv
import re
from datetime import datetime as dt

import Log.log as log
from Parser import utf8_validator
from Parser.db_func import db_commit_stock

data_path = utf8_validator.file_dump_path

def regexer(row):
    """
    Matches financial sector data like "^FINANCIAL" and "^PSEI" with data in row,
    A successful match function returns 'sector'.
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


def to_centavo(row_data):
    """
    Converts price_open, price_high, price_low, price_close to centavo
    SECTOR: name    trade_date, price_open, price_high, price_low, price_close, volume
    STOCK:  symbol  trade_date, price_open, price_high, price_low, price_close, volume
    :param list_object:
    :return:
    """
    #   Convert price_open to centavo
    row_data[2] = int(float(row_data[2]) * 100)
    #   Convert price_high to centavo
    row_data[3] = int(float(row_data[3]) * 100)
    #   Convert price_low to centavo
    row_data[4] = int(float(row_data[4]) * 100)
    #   Convert price_close to centavo
    row_data[5] = int(float(row_data[5]) * 100)
    return row_data


def to_integer(row_data):
    """
    Returns an integer for list[6], list[7].
    SECTOR: name, trade_date, price_open, price_high, price_low, price_close, volume
    STOCK:  symbol  trade_date, price_open, price_high, price_low, price_close, volume
    :param list_object:
    :return:
    """
    #   Convert volume to integer
    row_data[6] = int(row_data[6])
    return row_data


def to_date(row_data):
    """
    Converts string representation of Date to DateTime object
    Returns a datetime object for list[1]
    SECTOR: name, trade_date, price_open, price_high, price_low, price_close, volume
    STOCK:  symbol  trade_date, price_open, price_high, price_low, price_close, volume
    :param list_object:
    :return:
    """
    print(row_data)
    row_data[1] = dt.strftime(dt.strptime(row_data[1], "%m/%d/%Y"), "%Y-%m-%d")
    return row_data


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

            sector_name = None
            for row in all_rows:
                if regexer(row) == 'sector':
                    #   Perform type conversions
                    # row = to_date(to_centavo(to_integer(row[:-1])))

                    #   Populate models.Sector Instance Variables
                    # db_commit_sector(row)
                    # sector_name = row[0]
                    #sector_counter += 1
                    parser_log.info(f'Sector {row[0][1:]} data found on {file}')

                else:
                    #   Perform type conversions
                    row = to_date(to_centavo(to_integer(row[:-1])))
                    #   Populate models.Stock Instance Variables
                    if db_commit_stock(row) == 'duplicate':
                        parser_log.info(f'Data for {row[0]} already in DB. Duplicate on {file}')
                    else:
                        stock_counter += 1
                        parser_log.info(f'Stock {row[0]} data found on {file}')

            parser_log.info(f'{file} parsed successfully.')
            parser_log.info(f'STATISTICS for {file} : {sector_counter} sector data. {stock_counter} stock data.')


parser_log = log.get_logger(__name__)

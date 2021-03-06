# !/usr/bin/env python3.7

from datetime import datetime as dt

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import Log.log as log
from Parser import models
from Parser.db_base import Base
from Parser.db_config import *
from .models import Stock

db_logger = log.get_logger(__name__)

date_format = "%Y-%m-%d"

engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}', echo=True)

Base.metadata.create_all(engine, checkfirst=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def db_commit_sector(row):
    """
    Reads items in list passed by data_sorter() function
    Populates Sector class instance
    Commits data to appropriate table in db
    :param row:
    :return:
    """
    for item in row:
        name = row[0][1:]
        trade_date = dt.strftime(dt.strptime(row[1], date_format), date_format)
        price_open = row[2]
        price_high = row[3]
        price_low = row[4]
        price_close = row[5]
        volume = row[6]

    row = models.Sector(name, trade_date, price_open, price_high, price_low, price_close, volume)

    session.add(row)
    session.commit()
    db_logger.info(f'Commit Done. Sector: {row.name}    Trade date:  {row.trade_date} ')
    session.close()
    return row


def db_commit_stock(row):
    """
    Reads items in list passed by data_sorter() function
    Populates Stock class instance
    Commits data to appropriate table in db
    :param row:
    :return:
    """
    duplicate_stock = None

    for item in row:
        symbol = row[0]
        trade_date = dt.strftime(dt.strptime(row[1], date_format), date_format)
        price_open = row[2]
        price_high = row[3]
        price_low = row[4]
        price_close = row[5]
        volume = row[6]
        stock_id = symbol + trade_date.replace('-', '')

    db_entry = Stock(stock_id, symbol, trade_date, price_open, price_high, price_low, price_close, volume)

    ### IF EXISTS, Ignore
    # first get the object from the database if it exists
    # IF stock_ id is None, then Create a new record and log
    # otherwise, just log duplicates

    if session.query(Stock).filter(Stock.stock_id == stock_id).first() is None:
        unique_db_entry = Stock(stock_id, symbol, trade_date, price_open, price_high, price_low, price_close, volume)

        session.add(unique_db_entry)
        session.commit()
        db_logger.info(f'Commit Done. Stock: {unique_db_entry.symbol}    Trade date:  {unique_db_entry.trade_date} ')
        session.close()
        return unique_db_entry

    else:
        duplicate_stock = 'duplicate'
        db_logger.info(f'Duplicate Found: {db_entry.symbol}    Trade date:  {db_entry.trade_date}.  NO COMMIT')

        return duplicate_stock

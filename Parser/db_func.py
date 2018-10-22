# !/usr/bin/env python3.7

import re
import Log.log as log
from Parser import models
from datetime import datetime as dt

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Parser.db_config import *
from Parser.db_base import Base

db_logger = log.get_logger(__name__)

date_format = "%Y-%m-%d"

engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}', echo=True)

Base.metadata.create_all(engine, checkfirst=True)
# db_logger.info(f'Table {Combination.__tablename__} created on {db_config.host} using the {db_config.database} database')
DBSession = sessionmaker(bind=engine)
session = DBSession()


def db_commit_sector(row):
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
    session.close()
    return row


def db_commit_stock(row):
    for item in row:
        symbol = row[0]
        trade_date = dt.strftime(dt.strptime(row[1], date_format), date_format)
        price_open = row[2]
        price_high = row[3]
        price_low = row[4]
        price_close = row[5]
        volume = row[6]

    row = models.Stock(symbol, trade_date, price_open, price_high, price_low, price_close, volume)

    session.add(row)
    session.commit()
    session.close()
    return row

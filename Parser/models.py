#   Resource:
#   https://stackoverflow.com/questions/7478403/sqlalchemy-classes-across-files/32358096
from sqlalchemy import Column, Integer, BigInteger, String, Date

from Parser.db_base import Base


class Sector(Base):
    ## Sector Data Class
    #   Price is represented as centavos.
    #   1 peso = 100 cent
    #   1894756 peso = 1894756 cent
    #   15647.85 peso = 1564785 cent
    # 	The plan is to use the API data model as it has complete information.
    #	Sector data from API and CSV differs in columns. Example: in CSV VOLUME is missing, while VALUE and NETFOREIGN
    #	have been truncated by [:-2].
    #
    #	Raw Sector Data from csv:	^FINANCIAL,03/31/2017,1824.9,1825.96,1819.9,1820.56,1404080,25899
    #	Delimited:					^FINANCIAL	03/31/2017	1824.9	1825.96	1819.9	1820.56		1404080	25899
    #	API data model 				name		<>			open	high	low		close	volume	value	Netforeign
    #	CSV data model				name	date			open	high	low		close	!volume	!value	!Netforeign
    #	Keys:						name	date			open	high	low		close	volume	value	Netforeign

    __tablename__ = 'sector'

    id = Column('sector_id', Integer, primary_key=True)
    name = Column('sector_name', String(15))
    trade_date = Column('sector_date', Date)
    price_open = Column('sector_price_open', Integer)
    price_high = Column('sector_price_high', Integer)
    price_low = Column('sector_price_low', Integer)
    price_close = Column('sector_price_close', Integer)
    volume = Column('sector_volume', BigInteger)

    def __init__(self, name, trade_date, price_open, price_high, price_low, price_close, volume):
        self.name = name
        self.trade_date = trade_date
        self.price_open = price_open
        self.price_high = price_high
        self.price_low = price_low
        self.price_close = price_close
        self.volume = volume

class Stock(Base):
    ## Stock Data Class
    ##	Stock data from API and CSV differs in columns. Example: in CSV BID, ASK and NETFOREING is missingmaking the data unreliable.
    #
    #	Raw Stock Data from csv:	AUB,03/31/2017,47.2,47.5,47.15,47.15,3000,0
    #	Delimited:					AUB		03/31/2017	47.2	47.5	47.15	47.15	3000	0
    #	API data model 				symbol	date		open	high	low		close	bid	ask	volume	value	Netforeign
    #	CSV data model				symbol	date		open	high	low		close	!bid	!ask	volume	!value	Netforeign
    #	Keys:						symbol	date		open	high	low		close	bid	ask	volume	value	Netforeign sector

    __tablename__ = 'stock'

    id = Column('stock_id', Integer, primary_key=True)
    symbol = Column('stock_symbol', String(17))
    trade_date = Column('stock_date', Date)
    price_open = Column('stock_price_open', Integer)
    price_high = Column('stock_price_high', Integer)
    price_low = Column('stock_price_low', Integer)
    price_close = Column('stock_price_close', Integer)
    volume = Column('stock_volume', BigInteger)

    def __init__(self, stock_id, symbol, trade_date, price_open, price_high, price_low, price_close, volume):
        self.stock_id = stock_id
        self.symbol = symbol
        self.trade_date = trade_date
        self.price_open = price_open
        self.price_high = price_high
        self.price_low = price_low
        self.price_close = price_close
        self.volume = volume

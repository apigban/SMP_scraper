import requests
import Log.log as log
import concurrent.futures
from time import time

download_logger = log.get_logger(__name__)

attachment_id_start = 2708
attachment_id_end = 3738

attachment_id_list = list(range(attachment_id_start, attachment_id_end))

uri = 'http://www.stockmarketpilipinas.com/attachment.php?aid='


def uri_creator(base_uri, start, end, id_list):
    uri_list = []

    for attachment_id in attachment_id_list:
        uri_list.append(uri + str(attachment_id))

    print(uri_list)
    return uri_list


uri_creator(uri, attachment_id_start, attachment_id_end, attachment_id_list)

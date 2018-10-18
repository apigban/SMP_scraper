import requests
import Log.log as log
import concurrent.futures
from time import time

download_logger = log.get_logger(__name__)

attachment_id_start = 2708
attachment_id_end = 3739

attachment_id_list = list(range(attachment_id_start, attachment_id_end))

uri = 'http://www.stockmarketpilipinas.com/attachment.php?aid='


def uri_creator(base_uri, start, end, id_list):
    uri_list = []

    for attachment_id in attachment_id_list:
        uri_list.append(uri + str(attachment_id))

    download_logger.info(f'URI List Generated for attachment ids: [{attachment_id_start},{attachment_id_end}]')
    return uri_list


def download(download_list):
    for link in download_links:
        download_logger.info(f'Downloading link {link}')
        requests = requests.get(link)
        with open(f'dump/{attachment_id}.csv', 'wb') as attachment:
            attachment.write(requests.content)
        download_logger.info(f'Link Downloaded.')


download_links = uri_creator(uri, attachment_id_start, attachment_id_end, attachment_id_list)

download(download_links)

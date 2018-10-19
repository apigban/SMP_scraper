import re
import requests
import Log.log as log
from concurrent.futures import ThreadPoolExecutor as TPE
from concurrent.futures import as_completed
import time
import random


def uri_creator(uri, attachment_id_start, attachment_id_end, attachment_id_list):
    """
    Creates a uri_list from base_url and sequential attachment id
    :param base_uri: Stock Market Pilipinas start link http://www.stockmarketpilipinas.com/attachment.php?aid=
    :param start: Integer, Starting Attachment id for the file, used for iterator
    :param end: Integer, Ending Attachment id for the, used for iterator
    :param id_list:
    :return:
    """
    uri_list = []

    for attachment_id in attachment_id_list:
        uri_list.append(uri + str(attachment_id))

    download_logger.info(f'URI List Generated for attachment ids: [{attachment_id_start},{attachment_id_end}]')
    return uri_list


def downloader(link):
    pattern = r'(aid=)(\d+)$'
    attachment_id = re.search(pattern, link)
    filename = attachment_id.group(2)
    download_logger.info(f'Downloading Attachment: {filename} from {link} ')

    response = requests.get(link)
    with open(f'dump/{filename}.csv', 'wb') as attachment:
        attachment.write(response.content)

    download_logger.info(f'Attachment ID {filename} Downloaded.')
    time.sleep(random.randint(1, 8))
    return filename


def main(url_list):
    with TPE(max_workers=5) as executor:
        futures = [executor.submit(downloader, link) for link in url_list]
        for future in as_completed(futures):
            download_logger.info(f'Thread Closed for Attachment ID {future.result()}')


if __name__ == '__main__':
    download_logger = log.get_logger(__name__)

    attachment_id_start = 2708
    attachment_id_end = 3748

    attachment_id_list = list(range(attachment_id_start, attachment_id_end))

    uri = 'http://www.stockmarketpilipinas.com/attachment.php?aid='

    download_links = uri_creator(uri, attachment_id_start, attachment_id_end, attachment_id_list)

    main(download_links)

    download_logger.info(f'Downloaded {attachment_id_end - attachment_id_start} Attachments.')

import requests

CHECK_IP_SERVER_LIST = ['https://checkip.amazonaws.com',
                        'http://icanhazip.com', 'http://ip.cip.cc']


def get_external_ip():
    r"""get host external ip.
    :return: ip string
    """
    for url in CHECK_IP_SERVER_LIST:
        response = requests.get(url)
        if response.ok:
            return response.text.strip()
    return ''


if __name__ == '__main__':
    print(get_external_ip())

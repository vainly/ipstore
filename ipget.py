# -*- coding: utf-8 -*-

import requests
import bs4


def get_data_of_ip84(url):
    ip_list = []
    rsp = requests.get(url)
    print "request status : %s ", rsp.status_code
    soup = bs4.BeautifulSoup(rsp.text, "lxml")
    for tr in soup.find_all("tr"):
        data = []
        for td in tr.find_all("td"):
            data.append(td.text)
        ip_list.append(data)

    return ip_list


def get_ip84_url(num):
    url_list = []
    url = 'http://www.ip84.com/gn/'
    for i in range(1, num):
        url_list.append(url+str(i))
    return url_list


def ip84():
    num = 10
    ip_list = []
    url_list = get_ip84_url(num)
    for url in url_list:
        ip_list.append(get_data_of_ip84(url))

    print ip_list


if __name__ == "__main__":
    ip84()
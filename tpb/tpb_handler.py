#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Manozco
# @Date:   2014-08-01 22:20:45
# @Last Modified by:   Manozco
# @Last Modified time: 2014-08-01 22:26:29

from bs4 import BeautifulSoup
import requests

from tpb.constants import TPB_BASE_URL


class TpbHandler(object):
    def __init__(self):
        self.base_url = TPB_BASE_URL

    def seed_search(self, search_string):
        url = self.base_url + "{0}/0/7/0".format(search_string)
        ret = requests.get(url)
        soup = BeautifulSoup(ret.text)
        searchResults = soup.find(id='SearchResults')
        ret = {}
        for tr in searchResults.find_all('tr')[2:]:
            tds = tr.find_all('td')
            for td in tds:
                div = td.div
                link = td.find(title="Download this torrent using magnet")
                if link and div:
                    ret[div.a.string] = link['href']

        return ret

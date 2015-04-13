# -*- coding: utf-8 -*-

import re

from random import randrange
from urllib import unquote

from pyload.utils import json_loads
from pyload.plugin.internal.MultiHoster import MultiHoster


class FastixRu(MultiHoster):
    __name__    = "FastixRu"
    __type__    = "hoster"
    __version__ = "0.11"

    __pattern__ = r'http://(?:www\.)?fastix\.(ru|it)/file/\w{24}'
    __config__  = [("use_premium", "bool", "Use premium account if available", True)]

    __description__ = """Fastix multi-hoster plugin"""
    __license__     = "GPLv3"
    __authors__     = [("Massimo Rosamilia", "max@spiritix.eu")]


    def setup(self):
        self.chunkLimit = 3


    def handlePremium(self, pyfile):
        api_key = self.account.getAccountData(self.user)
        api_key = api_key['api']

        self.html = self.load("http://fastix.ru/api_v2/",
                         get={'apikey': api_key, 'sub': "getdirectlink", 'link': pyfile.url})

        data = json_loads(self.html)

        self.logDebug("Json data", data)

        if "error\":true" in self.html:
            self.offline()
        else:
            self.link = data['downloadlink']



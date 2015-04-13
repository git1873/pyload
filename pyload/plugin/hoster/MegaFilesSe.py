# -*- coding: utf-8 -*-

from pyload.plugin.internal.DeadHoster import DeadHoster


class MegaFilesSe(DeadHoster):
    __name__    = "MegaFilesSe"
    __type__    = "hoster"
    __version__ = "0.02"

    __pattern__ = r'http://(?:www\.)?megafiles\.se/\w{12}'
    __config__  = []

    __description__ = """MegaFiles.se hoster plugin"""
    __license__     = "GPLv3"
    __authors__     = [("t4skforce", "t4skforce1337[AT]gmail[DOT]com")]

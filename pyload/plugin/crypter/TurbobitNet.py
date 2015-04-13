# -*- coding: utf-8 -*-

import re

from pyload.plugin.internal.SimpleCrypter import SimpleCrypter
from pyload.utils import json_loads


class TurbobitNet(SimpleCrypter):
    __name__    = "TurbobitNet"
    __type__    = "crypter"
    __version__ = "0.05"

    __pattern__ = r'http://(?:www\.)?turbobit\.net/download/folder/(?P<ID>\w+)'
    __config__  = [("use_premium"       , "bool", "Use premium account if available"   , True),
                   ("use_subfolder"     , "bool", "Save package to subfolder"          , True),
                   ("subfolder_per_pack", "bool", "Create a subfolder for each package", True)]

    __description__ = """Turbobit.net folder decrypter plugin"""
    __license__     = "GPLv3"
    __authors__     = [("stickell", "l.stickell@yahoo.it"),
                       ("Walter Purcaro", "vuolter@gmail.com")]


    NAME_PATTERN = r'src=\'/js/lib/grid/icon/folder.png\'> <span>(?P<N>.+?)</span>'


    def _getLinks(self, id, page=1):
        gridFile = self.load("http://turbobit.net/downloadfolder/gridFile",
                             get={"rootId": id, "rows": 200, "page": page}, decode=True)
        grid = json_loads(gridFile)

        if grid['rows']:
            for i in grid['rows']:
                yield i['id']
            for id in self._getLinks(id, page + 1):
                yield id
        else:
            return


    def getLinks(self):
        id = re.match(self.__pattern__, self.pyfile.url).group('ID')
        fixurl = lambda id: "http://turbobit.net/%s.html" % id
        return map(fixurl, self._getLinks(id))

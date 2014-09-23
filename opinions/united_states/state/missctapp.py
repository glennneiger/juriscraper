"""Scraper for Mississippi Court of Appeals
CourtID: missctapp
Court Short Name: Miss. Ct. App.
Author: Jon Andersen
Reviewer:
Type: Precedential
History:
    2014-09-21: Created by Jon Andersen
"""


import time
from datetime import date
from lxml import html

from juriscraper.OpinionSite import OpinionSite
import miss

class Site(miss.Site):
    def __init__(self):
        super(Site, self).__init__()
        self.court_id = self.__module__
        self.url = 'http://courts.ms.gov/scripts/websiteX_cgi.exe/GetOpinion?Year=%s&Court=Court+of+Appeals&Submit=Submit' % date.today().year
        self.back_scrape_iterable = range(2013, 1996 - 1, -1)

    def _download_backwards(self, year):
        self.url = 'http://courts.ms.gov/scripts/websiteX_cgi.exe/GetOpinion?Year=%s&Court=Court+of+Appeals&Submit=Submit' % year
        self.html = self._download()

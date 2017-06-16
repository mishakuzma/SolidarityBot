"""
SolidarityBot Python Web Scraper

Attempts to extract relevant components from given web pages
to be used for SolidaryBot's email/newsletter.

Input: web address in URL form
Output: List of strings:
    -----
"""

# Use urllib2 to access web pages
# Use BeautifulSoup to access scraper functions

import urllib3
from bs4 import BeautifulSoup

0"""
SolidarityBot Python Web Scraper

Attempts to extract relevant components from given web pages
to be used for SolidaryBot's email/newsletter.

Input: web address in URL form
Output: List of strings:
    -----
"""

import

def main():
    # ----- URL Definition for the club's page -----
    urltodo = "http://www.testurl.com/"


    # ----- End of URL Definition -----

    # ----- Using urllib to access page elements -----
    # Pool manager needed to use library
    http = urllib3.PoolManager()

    # check for response code before accessing page
    r = http.request('GET',urltodo)
    if r.status != 200:
        return r.status
    else:
        pass

    """
    # extract JSON content (uncomment if relevant)
    json.loads(r.data.dcode('utf-8')
    
    """

    # page = urllib3.
    # ----- End of urllib usage -----

    # ----- Beautiful soup usage starts -----
    htmlSoup = BeautifulSoup(page,'html.parser') # Need url to be opened as page with html content

    # div class="tribe-events-event-cost (for cost of event

    timeDateStartRaw = htmlSoup.find_all("span", class="date-start dtstart") #returns list of all date-times
    for i in timeDateStartRaw:

    # ----- Beautiful soup usage ends

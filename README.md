#Scraper V2

* The old scraper is deprecated as the old site is not inaccessible
* New site is up and layout changed
* What should it do:
  # original page must be saved
  # process data from saved page
  # generate csv
  # generate json, which actually nice in some case
* Data pipeline
    Scraper -> HTML File(s) -> Processing Script 

## Requirements

* TOR SOCKS5 proxy (default when installing tor package on debian)
* python-yaml
* python-requests
* python-socks

## Running

1. fetcher.py (scrape)


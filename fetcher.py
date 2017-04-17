__author__ = 'sweemeng'
import requests
import socks
import socket
import yaml
import os
import random
import time
import logging
import sqlite3
import cPickle as pickle


MIN_PAGE_ID = 1
MAX_PAGE_ID = 257811

socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket

config = yaml.load(open("config.yaml"))

# TODO: Catch exception
def fetch_data():

    if not os.path.exists("stored.pickle"):
        processed_id = set()
    else:
        logging.warn("Load from pickle")
        pickled = open("stored.pickle")
        processed_id = pickle.load(pickled)
        pickled.close()
    # TODO: What if it is restarted
    contr_id = MIN_PAGE_ID
    while len(processed_id) < MAX_PAGE_ID:
        logging.warn("Processing id %s" % contr_id)
        if contr_id in processed_id:
            info_path = os.path.join(config["html_path"], "information_%s.html" % contr_id)
            project_path = os.path.join(config["html_path"], "project_%s.html" % contr_id)
            director_path = os.path.join(config["html_path"], "director_%s.html" % contr_id)
            # Just in case we deleted the file
            if os.path.exists(info_path) and os.path.exists(project_path):
                logging.warn("existing")
                contr_id += 1
                continue

        fetch_page("information", contr_id)
        fetch_page("project", contr_id)
        fetch_page("director", contr_id)
        logging.warn("Page stored")

        processed_id.add(contr_id)
        contr_id += 1
        time.sleep(1)
        pickle.dump(processed_id, open("stored.pickle", "w"))



def fetch_page(entity, entity_id):
    header = { "User-agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"}
    url = "%s%s/%s" % (config["base_url"], entity, entity_id)
    r = requests.get(url, headers=header)
    logging.warn("Fetching from URL %s" % url)
    if not r.status_code == 200:
        raise Exception("Exception occurred: %s, %s" % (r.status_code, r.content))
    file_name = "%s_%s.html" % (entity, entity_id)
    html_path = os.path.join(config["html_path"],file_name)
    f = open(html_path, "w")
    f.write(r.content)
    f.close()


if __name__ == "__main__":
    fetch_data()

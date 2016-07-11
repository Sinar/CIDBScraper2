__author__ = 'sweemeng'
from bs4 import BeautifulSoup
import os
import cPickle as pickle
import yaml


def process(html_file):
    soup = BeautifulSoup(html_file, 'html.parser')
    # TODO: process for project
    # TODO: process for profile


def get_file():
    config = yaml.load(open("config.yaml"))
    stored_html = config["stored_html"]
    items = os.listdir(stored_html)
    for item in items:
        f = open(os.path.join(stored_html, item))
        process(html_file=f)
        # TODO: project and information is processed differently
# -*- coding: utf-8 -*-
'''
    orgdisplay
    ~~~~~~~~~~

    Read org mode files and display them on static web pages.

    :copyright: (c) 2015 by Martin Stolle
    :license: no license.
'''
import argparse
import time

import orgparse

from flask import Flask
from flask import render_template

from watchdog import observers
from watchdog import events

#: `py:class:flask.Flask`
app = Flask(__name__)

sitecontent = None


@app.route('/')
def hello_world():
    return render_template('index.html', content=sitecontent)


def convert_to_html(content):
    '''

    :param content: `py:class:orgparse.node.OrgRootNode`
    '''
    global sitecontent
    sitecontent = content


def process_file(filename):
    ''' Start parser, read file, process content.

    :param filename: file to process
    :type param: str
    '''
    content = orgparse.load(filename)
    convert_to_html(content)


class OrgFilesHandler(events.PatternMatchingEventHandler):
    ''' EventHandler to watch all orgmode files.
    '''
    patterns = ['*.org']

    def on_modified(self, event):
        process_file(event.src_path)

    def on_created(self, event):
        process_file(event.src_path)


def serve(path):
    eventHandler = OrgFilesHandler()
    observer = observers.Observer()
    observer.schedule(eventHandler, path, recursive=False)
    observer.start()
    app.run(debug=True)
    observer.stop()
    observer.join()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Watch folder with org mode files.')
    parser.add_argument('-f', '--folder', default='.', nargs='?')
    args = parser.parse_args()
    serve(args.folder)

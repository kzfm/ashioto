# -*- encoding:utf-8 -*-
from datetime import datetime
import socket
import re
from twython import Twython
import os
import json
home = os.path.expanduser("~")
twitter_conf_file = os.path.join(home, '.ashioto', 'twitter.json')
tc = json.load(open(twitter_conf_file))

CONSUMER_KEY = tc["CONSUMER_KEY"]
CONSUMER_SECRET = tc["CONSUMER_SECRET"]
ACCESS_TOKEN = tc["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = tc["ACCESS_TOKEN_SECRET"]


class NameServer(object):
    def __init__(self, host="localhost", port=8000, buffer_size=8192, timeout=1):
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.timeout = timeout
        self.conn = None
        self.connected = False
        self.twitter = Twython(app_key=CONSUMER_KEY,
                               app_secret=CONSUMER_SECRET,
                               oauth_token=ACCESS_TOKEN,
                               oauth_token_secret=ACCESS_TOKEN_SECRET)

    def response_ok(self):
        self.conn.send('HTTP/1.0 200 OK\r\n\r\n')

    def tweet(self, name, title):
        songinfo = '♪ "{}" ({})'.format(title, name)
        print songinfo
        self.twitter.update_status(status=songinfo)

    def run(self):
        cue = SongCue(callback=self.tweet)
        artist_title_re = re.compile("ARTIST=(.*)TITLE=(.*)vorbis")
        print "NameServer start at {}:{}".format(self.host, self.port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen(1)
        conn, addr = s.accept()
        print 'Connected by', addr
        self.conn = conn

        while 1:
            data = conn.recv(8192)
            if not data: break
            if not self.connected:
                self.response_ok()
                self.connected = True
            at = artist_title_re.search(data)
            if at:
                name = at.group(1)
                title = at.group(2)
                cue.add(name, title)
            cue.noop()

        self.conn.close()
        print "NameServer stop"


class SongCue(object):
    def __init__(self, bytime=60, callback=None):
        self.bytime = bytime
        self.callback = callback
        self.new = {}

    def add(self, name, title):
        self.new["title"] = title
        self.new["name"] = name
        self.new["time"] = datetime.now()

    def noop(self):
        if "time" in self.new:
            dur = datetime.now() - self.new["time"]
            if dur.seconds > self.bytime:
                self.fire()

    def fire(self):
        self.callback(self.new["name"], self.new["title"])
        self.new = {}

if __name__ == '__main__':
    NameServer().run()

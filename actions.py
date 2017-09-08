#!/usr/bin/python
#author: Pavel Studenik
#email: studenik@varhoo.cz
import sys
import requests
import StringIO
from lxml.html import fromstring
import json

class RemoteDevice:
    def __init__(self, hostname, username, password):
        self.password=password
        self.username=username
        self.hostname=hostname
        self.conn = requests.session()

    def call(self, path):
        r = self.conn.post("http://%s/cgi-bin/%s" % (self.hostname, path), auth=(self.username, self.password), data={})
        return r

    def power_on(self):
        print "power on"
        r = self.call("power_on.cgi")

    def power_off(self):
        print "power off"
        r = self.call("power_off.cgi")

    def status(self):
        c = self.call("projector_status.cgi?lang=en")
        data = self.parse(c)
        return json.dumps(data))

    def parse(self, content):
        result = fromstring(content)
        data = {}
        for table in result.body:
            for tr in table:
                for td in tr:
                    row = [it.text_content().strip() for it in td[0][0]]
                    key = row[0].lower()
                    if "power" == key:
                        for it in  td[0][0][1]:
                            if it.attrib["color"] == "#00ff12":
                                row = [None, it.text_content().strip(),]
                    if not "".join(row[1:]):
                        continue
                    data[key] = "".join(row[1:])
        return data

def testing(filename):
    f = open(filename)
    c = f.read()
    f.close()
    rd = RemoteDevice(None, None, None)
    json.dumps(rd.parse(c))

if __name__=="__main__":
    # testing("status.1.html")
    # testing("status.2.html")
    rd = RemoteDevice(*sys.argv[1:3])
    print rd.status()

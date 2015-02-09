#!/usr/bin/python
#author: Pavel Studenik
#email: studenik@varhoo.cz
import requests
import StringIO
from lxml.html import fromstring

class RemoteDevice:
    def __init__(self, hostname, username, password):
        self.password=password
        self.username=username
        self.hostname=hostname
        self.conn = requests.session()

    def call(self, path):
        r = self.conn.post("http://%s/cgi-bin/%s" % (self.hostname, path), auth=(self.username, self.password), data={})
        print r
        return r

    def power_on(self):
        r = self.call("power_on.cgi")
        print "power on"

    def power_off(self):
        print "power off"
        r = self.call("power_off.cgi")

    def status(self):
        c = self.call("projector_status.cgi?lang=en")
        data = self.parse(c)
        for it in data:
            print it, ":", data[it]

    def parse(self, content):
        result = fromstring(content)
        data = {}
        for table in result.body:
            for tr in table:
                for td in tr:
                    row = [it.text_content().strip() for it in td[0][0]]
                    data[row[0]] = "".join(row[1:])
        return data

if __name__=="__main__":
    pass

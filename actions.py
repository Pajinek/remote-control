#!/usr/bin/python
#author: Pavel Studenik
#email: studenik@varhoo.cz
import requests

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
        r = self.call("projector_status.cgi?lang=en")

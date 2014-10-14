#!/usr/bin/python
#author: Pavel Studenik
#email: studenik@varhoo.cz
import requests

class RemoteDevice:
    def __init__(self, hostname, username, password):
        self.password=password
        self.username=username
        self.hostname=hostnam
        self.conn = requests.session()

    def call(self, path):
        r = self.conn.post("http://%s/cgi-bin/%s" % (self.hostname, path) 
                    auth=(self.username, self.password), data={})
        return r

    def power_on(self):
        r = self.call("power_on.cgi")

    def power_off(self):
        r = self.call("power_ff.cgi")

    def status(self):
        r = self.call("projector_status.cgi?lang=en")

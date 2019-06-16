#!/usr/bin/env python3
import paramiko
import os
import pwd
import json
from .GetProposal import GetProposal

class SyncData:
    def __init__(self):
        self.fullname=pwd.getpwuid(os.getuid())[4]
        self.username=self.fullname.replace(" ", ".").lower()
        self.get_config()

    def get_config(self):
        with open('config.json') as json_file:  
            data = json.load(json_file)
            self.hostname=data['hostname']

    def put(self):
        hostname = self.hostname
        print(hostname)
        username = self.username
        port = 22

        mypath='/data/kafka-to-nexus/nicos000187.hdf'
        mypath=os.getcwd()+'/x.txt'
        print(mypath)
        remotepath='/users/detector/experiments/V20/DEFAULT'

        prop = GetProposal()

        remote_directory = prop.fetch()
        print("remote_dir",remote_directory)
        remotepath='/users/'+username+'/x.txt'
        print(remotepath)

        from os.path import expanduser
        home = expanduser("~")
        t = paramiko.Transport((hostname, port))
        keyname=home+"/.ssh/id_ed25519"
        print(username)
        print(keyname)
        ed25519_key = paramiko.Ed25519Key.from_private_key_file(keyname)
        t.connect(username=username,  pkey=ed25519_key)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(mypath, remotepath)


if __name__ == "__main__":
    sync = SyncData()
    sync.put()
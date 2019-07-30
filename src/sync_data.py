#!/usr/bin/env python3
"""sync data"""
import os
import pwd
import logging
import json
import paramiko
from scp import SCPClient
from get_proposal import GetProposal
from get_files import GetFiles
from abstract_sync import AbstractSync


class SyncData(AbstractSync):
    """Sync data to remote machine"""

    def __init__(self):
        self.fullname = pwd.getpwuid(os.getuid())[4]
        # self.username=self.fullname.replace(" ", ".").lower()
        self.get_config()

    def get_config(self):
        """Read config from local json file"""
        with open('config.json') as json_file:
            data = json.load(json_file)
            self.hostname = data['hostname']
            self.username = data['username']
        return data

    def put(self):
        """sync data"""
        logging.basicConfig(level=logging.DEBUG)
        hostname = self.hostname
        print(hostname)
        username = self.username

        mypath = '/data/kafka-to-nexus/nicos000187.hdf'
        mypath = os.getcwd()+'/x.txt'
        print(mypath)
        basepath = '/users/detector/experiments/V20/'

        prop = GetProposal()
        file_mgr = GetFiles()
        file_mgr.set_base('./demo')
        file_array = file_mgr.get()

        remote_directory = basepath + prop.fetch()
        remote_directory = '/users/'+username + '/'
        print("remote_dir", remote_directory)

        from os.path import expanduser
        home = expanduser("~")
        ssh_config_file = os.path.expanduser("~/.ssh/config")
        proxy = None
        if os.path.exists(ssh_config_file):
            conf = paramiko.SSHConfig()
            with open(ssh_config_file) as ssh_conf:
                conf.parse(ssh_conf)
            host_config = conf.lookup('login')
            if 'proxycommand' in host_config:
                print(host_config['proxycommand'])
                proxy = paramiko.ProxyCommand(host_config['proxycommand'])
        keyname = home+"/.ssh/id_ed25519"
        print(username)
        print(keyname)
        ed25519_key = paramiko.Ed25519Key.from_private_key_file(keyname)

        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, username=username, pkey=ed25519_key, sock=proxy)
        scp = SCPClient(ssh.get_transport())
        for file in file_array:
            mypath = file
            basename = os.path.basename(mypath)
            remotepath = remote_directory + '/' + basename
            print(remotepath)
            scp.put(mypath, recursive=True, remote_path=remotepath)
        scp.close()


if __name__ == "__main__":
    SYNC = SyncData()
    SYNC.put()

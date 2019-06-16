#!/usr/bin/env python3
import requests
import json
import os
import pwd
import getpass
import keyring
import urllib.parse
import platform
import socket
import datetime


class GetProposal:
    username = "anonymoususer"
    name = "Anonymous User"
    email = "anonymous.user@mail.fjref.dk"

    def __init__(self):
        self.get_details()

    def fetch_login_from_keyring(self):
        if platform.system() == 'Darwin':
            print('darwin')
            username = "brightness"
            username = "ingestor"
            #username = self.username
            password = keyring.get_password('scicat', username)
            if not password:
                print("No password found in keychain, please enter it now to store it.")
                password = getpass.getpass()
                keyring.set_password('scicat', username, password)

            config = {"username": username, "password": password}
            print(config["username"])

        return config

    def get_details(self):
        self.username = getpass.getuser()
        self.name = pwd.getpwuid(os.getuid())[4]
        self.email = self.name.replace(" ", ".")+"@esss.se"
        self.hostname = socket.gethostname()

    def fetch(self):
        base_url = "https://scicatapi.esss.dk/"
        #if self.hostname == "CI0020036":
        #    base_url = "http://localhost:3000/"
        user_url = base_url + "auth/msad"
        api_url = base_url + "api/v3/"
        ingestor_url = api_url+"Users/login"
        login_url = ingestor_url

        if platform.system() == 'Darwin':
            config = self.fetch_login_from_keyring()
        else:
            password = getpass.getpass()
            config = {"username": self.username, "password": password}
        #config = self.fetch_login_from_keyring()

        print(login_url)
        r = requests.post(login_url, data=config)

        login_response = r.json()
        print(login_response)
        if "id" in login_response:
            token = login_response["id"]
        elif "access_token" in login_response:
            token = login_response["access_token"]
        else:
            print("Login failed - exiting")
            exit()

        instrument = "V20"
        measureTime = "2019-06-16T04:17:06.237Z"
        measureTime = datetime.datetime.now().isoformat()
        dataset_url = api_url + "Proposals/findByInstrumentAndDate?instrument=" + \
            instrument + "&measureTime=" + measureTime + "&access_token="+token

        print(dataset_url)
        r = requests.get(dataset_url)
        prop = r.json()
        print(prop)
        proposal_id ="DEFAULT"
        if 'findByInstrumentAndDate' in prop:
            result=prop['findByInstrumentAndDate']
            if 'proposalId' in result:
                proposal_id = result['proposalId']
        return proposal_id


if __name__ == "__main__":
    scicatman = GetProposal()
    scicatman.fetch()

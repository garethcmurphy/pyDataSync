#!/usr/bin/env python3
"""Fetch proposal"""
import os
import pwd
import getpass
import platform
import socket
import datetime
import json

import keyring
import requests

class GetProposal:
    """fetch proposal from scicat"""
    username = "anonymoususer"
    name = "Anonymous User"
    email = "anonymous.user@mail.fjref.dk"

    def __init__(self):
        self.get_details()

    def get_config(self):
        """get config from json file"""
        with open('user.json') as json_file:
            data = json.load(json_file)
            return data

    def fetch_login_from_keyring(self):
        """if on darwin fetch login from keyring"""
        if platform.system() == 'Darwin':
            print('darwin')
            username = "brightness"
            username = "ingestor"
            # username = self.username
            password = keyring.get_password('scicat', username)
            if not password:
                print("No password found in keychain, please enter it now to store it.")
                password = getpass.getpass()
                keyring.set_password('scicat', username, password)

            config = {"username": username, "password": password}
            print(config["username"])

        return config

    def get_details(self):
        """get details from os"""
        self.username = getpass.getuser()
        self.name = pwd.getpwuid(os.getuid())[4]
        self.email = self.name.replace(" ", ".")+"@esss.se"
        self.hostname = socket.gethostname()
        return self.hostname

    def fetch(self):
        """fetch proposal from scicat"""
        base_url = "https://scicatapi.esss.dk/"
        # if self.hostname == "CI0020036":
        #    base_url = "http://localhost:3000/"
        user_url = base_url + "auth/msad"
        api_url = base_url + "api/v3/"
        ingestor_url = api_url+"Users/login"
        login_url = ingestor_url

        if platform.system() == 'Darwin':
            config = self.fetch_login_from_keyring()
        else:
            # password = getpass.getpass()
            # config = {"username": self.username, "password": password}
            config = self.get_config()
        # config = self.fetch_login_from_keyring()

        print(login_url)
        response = requests.post(login_url, data=config)

        login_response = response.json()
        print(login_response)
        if "id" in login_response:
            token = login_response["id"]
        elif "access_token" in login_response:
            token = login_response["access_token"]
        else:
            print("Login failed - exiting")
            exit()

        instrument = "V20"
        measure_time = datetime.datetime.now().isoformat()
        dataset_url = api_url + "Proposals/findByInstrumentAndDate?instrument=" + \
            instrument + "&measureTime=" + measure_time + "&access_token="+token

        print(dataset_url)
        response = requests.get(dataset_url)
        prop = response.json()
        print(prop)
        proposal_id = "DEFAULT"
        if 'findByInstrumentAndDate' in prop:
            result = prop['findByInstrumentAndDate']
            if 'proposalId' in result:
                proposal_id = result['proposalId']
        return proposal_id


if __name__ == "__main__":
    SCI = GetProposal()
    SCI.fetch()

#!/usr/bin/env python3
"""add files via rsync"""
import subprocess
from AbstractSync import AbstractSync
from get_files import GetFiles


class RsyncSystem(AbstractSync):
    """add files via rsync"""
    input = "input/"
    file_array = []

    def fetch_files(self):
        file_mgr = GetFiles()
        file_mgr.set_base('./demo')
        self.file_array = file_mgr.get()

    def put(self):
        print(self.input)
        local = " --include=".join(self.file_array)
        remote_dir = "login:v20"
        subprocess.run(["echo", "rsync", "-avz", "--include=" +
                        local, "--exclude='*'", remote_dir])

    def main(self):
        self.fetch_files()
        self.put()


if __name__ == "__main__":
    pass
    rsync = RsyncSystem()
    rsync.main()

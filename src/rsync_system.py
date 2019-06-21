#!/usr/bin/env python3
"""add files via rsync"""
import subprocess
from abstract_sync import AbstractSync
from get_files import GetFiles


class RsyncSystem(AbstractSync):
    """add files via rsync"""
    input = "input/"
    file_array = []

    def fetch_files(self):
        """fetch files"""
        file_mgr = GetFiles()
        file_mgr.set_base('./demo')
        self.file_array = file_mgr.get()

    def put(self):
        """put files via system call to rsync"""
        print(self.input)
        local = " --include=".join(self.file_array)
        remote_dir = "login:v20"
        subprocess.run(["echo", "rsync", "-avz", "--include=" +
                        local, "--exclude='*'", remote_dir])

    def main(self):
        """main program"""
        self.fetch_files()
        self.put()


if __name__ == "__main__":
    R = RsyncSystem()
    R.main()

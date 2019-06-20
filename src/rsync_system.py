import subprocess

class RsyncSystem:
    input = "input/"
    pass

    def get(self):
        print(self.input)
        subprocess.run(["rsync", "-l"])
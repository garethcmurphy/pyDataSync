#!/usr/bin/env python3
import datetime 
import os

class GetFiles:
    def get(self):
        now = datetime.datetime.now()
        ago = now-datetime.timedelta(minutes=60)

        search_directory = "/data/kafka-to-nexus"
        search_directory = "./demo"


        for root, dirs, files in os.walk(search_directory):
            for fname in files:
                path = os.path.join(root, fname)
                st = os.stat(path)
                mtime = datetime.datetime.fromtimestamp(st.st_mtime)
                if mtime > ago:
                    print('%s modified %s' % (path, mtime))
                pass


if __name__ == "__main__":
    file_get = GetFiles()
    file_get.get()
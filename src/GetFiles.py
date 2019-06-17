#!/usr/bin/env python3
import datetime
import os


class GetFiles:
    """Fetch recently modified files"""
    base_directory = "string"
    
    def get(self):
        now = datetime.datetime.now()
        ago = now-datetime.timedelta(minutes=60)

        search_directory = "/data/kafka-to-nexus"
        search_directory = os.getcwd()+"/demo"

        file_array = list()

        for root, dirs, files in os.walk(search_directory):
            for fname in files:
                path = os.path.join(root, fname)
                st = os.stat(path)
                mtime = datetime.datetime.fromtimestamp(st.st_mtime)
                if mtime > ago:
                    file_array.append(path)
                    print('%s modified %s' % (path, mtime))
                else:
                    print('%s modified %s' % (path, mtime))

        return file_array


if __name__ == "__main__":
    file_mgr = GetFiles()
    file_array = file_mgr.get()
    print(file_array)

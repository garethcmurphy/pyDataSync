#!/usr/bin/env python3
import datetime
import os


class GetFiles:
    """Fetch recently modified files"""
    base_directory = "/data/kafka-to-nexus"

    def get(self):
        """fetch recently modified files"""
        now = datetime.datetime.now()
        ago = now-datetime.timedelta(minutes=60)

        if os.path.isdir(self.base_directory):
            search_directory = self.base_directory
        else:
            search_directory = os.getcwd()+"/demo"

        file_array = list()

        for root, dirs, files in os.walk(search_directory):
            for fname in files:
                path = os.path.join(root, fname)
                stat_info = os.stat(path)
                mtime = datetime.datetime.fromtimestamp(stat_info.st_mtime)
                if mtime > ago:
                    file_array.append(path)
                    print('%s modified %s' % (path, mtime))
                else:
                    print('%s modified %s' % (path, mtime))

        return file_array


if __name__ == "__main__":
    FILEMGR = GetFiles()
    file_array2 = FILEMGR.get()
    print(file_array2)

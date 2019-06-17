
import sys, os
sys.path.append("./src")

from GetFiles import GetFiles
def test_sync():

    sync = GetFiles()
    assert( isinstance( sync.base_directory ,str) )

import sys, os
sys.path.append("./src")

from SyncData import SyncData
def test_sync():

    sync = SyncData()
    conf =sync.get_config()
    assert( isinstance( conf['hostname' ],str) )
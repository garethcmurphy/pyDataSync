
from .SyncData import SyncData
def test_sync():

    sync = SyncData()
    conf =sync.get_config()
    assert( 'hostname' in conf)
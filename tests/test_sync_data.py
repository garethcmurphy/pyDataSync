"""unit test"""
import sys
sys.path.append("./src")

from SyncData import SyncData

def test_sync():
    """unit test"""
    sync = SyncData()
    conf = sync.get_config()
    assert(isinstance(conf['hostname'], str))

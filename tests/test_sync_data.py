"""unit test"""

from sync_data import SyncData


def test_sync():
    """unit test"""
    sync = SyncData()
    conf = sync.get_config()
    assert isinstance(conf['hostname'], str)

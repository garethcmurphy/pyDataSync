import sys
sys.path.append("./src")
from get_files import GetFiles


def test_sync():

    sync = GetFiles()
    assert isinstance(sync.base_directory, str)

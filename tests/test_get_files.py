"""unit test"""
import sys
sys.path.append("./src")
from get_files import GetFiles


def test_sync():
    """unit test sync"""

    sync = GetFiles()
    assert isinstance(sync.base_directory, str)

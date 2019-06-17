"""unit test"""
import sys
import conftest
#sys.path.append("./src")
from get_files import GetFiles


def test_sync():
    """unit test sync"""

    sync = GetFiles()
    assert isinstance(sync.base_directory, str)

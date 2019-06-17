
import sys
sys.path.append("./src")
from get_proposal import GetProposal


def test_sync():

    sync = GetProposal()
    conf = sync.get_details()
    assert(isinstance(conf, str))

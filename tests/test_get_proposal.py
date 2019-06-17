
import sys, os
sys.path.append("./src")

from GetProposal import GetProposal
def test_sync():

    sync = GetProposal()
    conf =sync.get_details()
    assert( isinstance( conf,str) )
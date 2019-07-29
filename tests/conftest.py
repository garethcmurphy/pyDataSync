"""configure tests"""
import sys
sys.path.append("./src")


def pytest_runtest_setup(item):
    """unneeded test function"""
    # called for running each test in 'a' directory
    print("setting up", item)

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from myfile import MyFile
def test_add():
    mf = MyFile()
    a = mf.add_numbers(2,3)
    assert a == 4
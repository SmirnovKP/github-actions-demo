import sys
sys.path.append('src')
import hello
def test_add_7():
    assert hello.add(7, 7) == 14
def test_add_7_negative():
    assert hello.add(-7, -7) == -14

import sys
sys.path.append('src')
import hello
def test_add_11():
    assert hello.add(11, 11) == 22
def test_add_11_negative():
    assert hello.add(-11, -11) == -22

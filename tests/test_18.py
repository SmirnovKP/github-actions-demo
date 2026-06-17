import sys
sys.path.append('src')
import hello
def test_add_18():
    assert hello.add(18, 18) == 36
def test_add_18_negative():
    assert hello.add(-18, -18) == -36

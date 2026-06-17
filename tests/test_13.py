import sys
sys.path.append('src')
import hello
def test_add_13():
    assert hello.add(13, 13) == 26
def test_add_13_negative():
    assert hello.add(-13, -13) == -26

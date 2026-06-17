import sys
sys.path.append('src')
import hello
def test_add_1():
    assert hello.add(1, 1) == 2
def test_add_1_negative():
    assert hello.add(-1, -1) == -2

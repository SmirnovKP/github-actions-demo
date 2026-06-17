import sys
sys.path.append('src')
import hello
def test_add_9():
    assert hello.add(9, 9) == 18
def test_add_9_negative():
    assert hello.add(-9, -9) == -18

import sys
sys.path.append('src')
import hello
def test_add_14():
    assert hello.add(14, 14) == 28
def test_add_14_negative():
    assert hello.add(-14, -14) == -28

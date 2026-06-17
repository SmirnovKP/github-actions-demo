import sys
sys.path.append('src')
import hello
def test_add_6():
    assert hello.add(6, 6) == 12
def test_add_6_negative():
    assert hello.add(-6, -6) == -12

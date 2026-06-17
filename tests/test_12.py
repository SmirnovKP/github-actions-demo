import sys
sys.path.append('src')
import hello
def test_add_12():
    assert hello.add(12, 12) == 24
def test_add_12_negative():
    assert hello.add(-12, -12) == -24

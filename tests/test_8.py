import sys
sys.path.append('src')
import hello
def test_add_8():
    assert hello.add(8, 8) == 16
def test_add_8_negative():
    assert hello.add(-8, -8) == -16

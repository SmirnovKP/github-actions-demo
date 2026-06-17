import sys
sys.path.append('src')
import hello
def test_add_4():
    assert hello.add(4, 4) == 8
def test_add_4_negative():
    assert hello.add(-4, -4) == -8

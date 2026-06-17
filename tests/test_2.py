import sys
sys.path.append('src')
import hello
def test_add_2():
    assert hello.add(2, 2) == 4
def test_add_2_negative():
    assert hello.add(-2, -2) == -4

import sys
sys.path.append('src')
import hello
def test_add_3():
    assert hello.add(3, 3) == 6
def test_add_3_negative():
    assert hello.add(-3, -3) == -6

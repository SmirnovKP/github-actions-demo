import sys
sys.path.append('src')
import hello
def test_add_10():
    assert hello.add(10, 10) == 20
def test_add_10_negative():
    assert hello.add(-10, -10) == -20

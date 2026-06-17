import sys
sys.path.append('src')
import hello
def test_add_5():
    assert hello.add(5, 5) == 10
def test_add_5_negative():
    assert hello.add(-5, -5) == -10

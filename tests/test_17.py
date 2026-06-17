import sys
sys.path.append('src')
import hello
def test_add_17():
    assert hello.add(17, 17) == 34
def test_add_17_negative():
    assert hello.add(-17, -17) == -34

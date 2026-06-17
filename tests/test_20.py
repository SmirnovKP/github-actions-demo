import sys
sys.path.append('src')
import hello
def test_add_20():
    assert hello.add(20, 20) == 40
def test_add_20_negative():
    assert hello.add(-20, -20) == -40

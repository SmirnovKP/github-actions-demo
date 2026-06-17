import sys
sys.path.append('src')
import hello
def test_add_15():
    assert hello.add(15, 15) == 30
def test_add_15_negative():
    assert hello.add(-15, -15) == -30

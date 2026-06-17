import sys
sys.path.append('src')
import hello
def test_add_19():
    assert hello.add(19, 19) == 38
def test_add_19_negative():
    assert hello.add(-19, -19) == -38

import sys
sys.path.append('src')
import hello
def test_add_16():
    assert hello.add(16, 16) == 32
def test_add_16_negative():
    assert hello.add(-16, -16) == -32

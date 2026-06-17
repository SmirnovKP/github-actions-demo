import sys
sys.path.append('src')
import hello
def test_say_hello():
    assert hello.say_hello("World") == "Hello, World!"
def test_add():
    assert hello.add(2, 3) == 5
    assert hello.add(-1, 1) == 0

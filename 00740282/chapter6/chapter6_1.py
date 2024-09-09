'''
完善例 6.8 的实现。为数偶类 Couple 提供属性存取方法.

```python
# 【例6.8】定义整数数偶类 Couple。其有两个整数属性 _1 与 _2。定义初始化方法，设置 _1 与 _2 的初始值，缺省时均设置为 0。
class Couple:
    """A simple integer couple class definition

    Attributes:
        _1: The first field of an integer couple, initialized with 0.
        _2: The second field of an integer couple, initialized with 0.

    Functions:
        __init__(self, x = 0, y = 0) -> None:
            Use x and y to initialize the integer couple, self.
        Parameters:
            self: The object per se.
            x: An integer, 0 as its default argument value.
            y: An integer, 0 as its default argument value.
        Returned value:
            None.

    f(self) -> str:
        Get the string representation of the integer couple.
        Parameter:
            self: The object per se.
        Returned value:
            A string representation with the integer couple (x, y).
    """
'''

class Couple:
    """
    A simple integer couple class definition

    Attributes:
        _1: The first field of an integer couple, initialized with 0.
        _2: The second field of an integer couple, initialized with 0.

    Functions:
        __init__(self, x = 0, y = 0) -> None:
            Use x and y to initialize the integer couple, self.
        Parameters:
            self: The object per se.
            x: An integer, 0 as its default argument value.
            y: An integer, 0 as its default argument value.
        Returned value:
            None.

        f(self) -> str:
            Get the string representation of the integer couple.
            Parameter:
                self: The object per se.
            Returned value:
                A string representation with the integer couple (x, y).

        get_1(self) -> int:
            Get the value of the first field.
            Parameter:
                self: The object per se.
            Returned value:
                The value of the first field.

        get_2(self) -> int:
            Get the value of the second field.
            Parameter:
                self: The object per se.
            Returned value:
                The value of the second field.

        set_1(self, x: int) -> None:
            Set the value of the first field.
            Parameters:
                self: The object per se.
                x: An integer, the value to be set.
            Returned value:
                None.

        set_2(self, y: int) -> None:
            Set the value of the second field.
            Parameters:
                self: The object per se.
                y: An integer, the value to be set.
            Returned value:
                None.
    """

    def __init__(self, x = 0, y = 0) -> None:
        '''Use x and y to initialize the integer couple, self.'''
        self._1 = x
        self._2 = y

    def f(self) -> str:
        '''Get the string representation of the integer couple.'''
        return f"I'm ({self._1}, {self._2})!"

    def get_1(self) -> int:
        '''Get the value of the first field.'''
        return self._1

    def get_2(self) -> int:
        '''Get the value of the second field.'''
        return self._2

    def set_1(self, x: int) -> None:
        '''Set the value of the first field.'''
        self._1 = x

    def set_2(self, y: int) -> None:
        '''Set the value of the second field.'''
        self._2 = y

def test_couple():
    '''Test the couple class.'''
    # Create a couple object with default values
    couple = Couple()
    assert couple.get_1() == 0
    assert couple.get_2() == 0
    print("Test default values passed.")

    # Set new values for the couple object
    couple.set_1(10)
    couple.set_2(20)
    assert couple.get_1() == 10
    assert couple.get_2() == 20
    print("Test set values passed.")

    # Create a couple object with custom values
    couple = Couple(5, 15)
    assert couple.get_1() == 5
    assert couple.get_2() == 15
    print("Test custom values passed.")

    # Test the string representation of the couple object
    assert couple.f() == "I'm (5, 15)!"
    print("Test string representation passed.")

    print("All tests passed.")

def main():
    '''Main function'''
    test_couple()

if __name__ == "__main__":
    main()

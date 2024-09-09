'''
继续上一题。为数偶类 Couple 定制格式化方法和转换为字符串的方法。
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

        __str__(self) -> str:
            Get the informal string representation of the integer couple.
            Parameters:
                self: The object per se.
            Returned value:
                A string representation with the integer couple: (x, y).

        __repr__(self) -> str:
            Get the official string representation of the integer couple.
            Parameters:
                self: The object per se.
            Returned value:
                A string representation with the integer couple: Couple(x, y).

        format(self, format_spec: str = '') -> str:
            Custom format method to allow formatting of the integer couple.
            Parameters:
                self: The object per se.
                format_spec: A string specifying the format.
            Returned value:
                A formatted string representation of the integer couple.
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

    def __str__(self) -> str:
        '''Get the informal string representation of the integer couple.'''
        return f"({self._1}, {self._2})"

    def __repr__(self) -> str:
        '''Get the official string representation of the integer couple.'''
        return f"Couple(x={self._1}, y={self._2})"

    def format(self, format_spec: str = '') -> str:
        '''Custom format method to allow formatting of the integer couple.'''
        if not format_spec:
            return f"({self._1}, {self._2})"
        try:
            return f"({self._1:{format_spec}}, {self._2:{format_spec}})"
        except ValueError:
            return f"Invalid format string: {format_spec}"

def test_couple():
    '''Test the Couple class.'''
    c = Couple(3, 4)
    assert str(c) == "(3, 4)"
    assert repr(c) == "Couple(x=3, y=4)"
    assert c.format() == "(3, 4)"
    assert c.format("002") == "(03, 04)"
    print("All tests passed.")

def main():
    '''Main function for the test.'''
    test_couple()

if __name__ == "__main__":
    main()

'''
继续上一题。为数偶类 Couple 定制比较方法。
两个数偶的比较规则是：首先比较 _1 属性，其次比较 _2 属性。
两个属性都相等时，数偶相等；否则不等。
两者的大小关系则由 _1 属性的大小关系确定；_1 属性相等时，由 _2 属性的大小关系确定。
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

        __eq__(self, other: 'Couple') -> bool:
            Compare if two Couples are equal.
            Parameters:
                self: The object per se.
                other: Another Couple object to compare with.
            Returned value:
                True if both _1 and _2 are equal, False otherwise.

        __ne__(self, other: 'Couple') -> bool:
            Compare if two Couples are not equal.
            Parameters:
                self: The object per se.
                other: Another Couple object to compare with.
            Returned value:
                True if either _1 or _2 are not equal, False otherwise.

        __lt__(self, other: 'Couple') -> bool:
            Compare if self is less than other.
            Parameters:
                self: The object per se.
                other: Another Couple object to compare with.
            Returned value:
                True if self._1 is less than other._1, or\\
                if self._1 is equal to other._1 and self._2 is less than other._2.

        __le__(self, other: 'Couple') -> bool:
            Compare if self is less than or equal to other.
            Parameters:
                self: The object per se.
                other: Another Couple object to compare with.
            Returned value:
                True if self._1 is less than or equal to other._1, or\\
                if self._1 is equal to other._1 and self._2 is less than or equal to other._2.

        __gt__(self, other: 'Couple') -> bool:
            Compare if self is greater than other.
            Parameters:
                self: The object per se.
                other: Another Couple object to compare with.
            Returned value:
                True if self._1 is greater than other._1, or\\
                if self._1 is equal to other._1 and self._2 is greater than other._2.

        __ge__(self, other: 'Couple') -> bool:
            Compare if self is greater than or equal to other.
            Parameters:
                self: The object per se.
                other: Another Couple object to compare with.
            Returned value:
                True if self._1 is greater than or equal to other._1, or\\
                if self._1 is equal to other._1 and self._2 is greater than or equal to other._2.
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

    def __eq__(self, other: 'Couple') -> bool:
        '''Compare if two Couples are equal.'''
        return self._1 == other._1 and self._2 == other._2

    def __ne__(self, other: 'Couple') -> bool:
        '''Compare if two Couples are not equal.'''
        return self._1 != other._1 or self._2 != other._2

    def __lt__(self, other: 'Couple') -> bool:
        '''Compare if self is less than other.'''
        return self._1 < other._1 or (self._1 == other._1 and self._2 < other._2)

    def __le__(self, other: 'Couple') -> bool:
        '''Compare if self is less than or equal to other.'''
        return self._1 < other._1 or (self._1 == other._1 and self._2 <= other._2)

    def __gt__(self, other: 'Couple') -> bool:
        '''Compare if self is greater than other.'''
        return self._1 > other._1 or (self._1 == other._1 and self._2 > other._2)

    def __ge__(self, other: 'Couple') -> bool:
        '''Compare if self is greater than or equal to other.'''
        return self._1 > other._1 or (self._1 == other._1 and self._2 >= other._2)

def test_couple():
    '''Test the Couple class.'''
    a = Couple(3, 4)
    b = Couple(3, 4)
    assert a == b
    assert a <= b
    assert a >= b
    assert not a != b
    assert not a < b
    assert not a > b
    print("Couple equality test passed.")

    a = Couple(3, 4)
    b = Couple(3, 5)
    assert a != b
    assert a < b
    assert a <= b
    assert not a == b
    assert not a > b
    assert not a >= b
    print("Couple less than test passed.")

    a = Couple(3, 4)
    b = Couple(2, 4)

    assert a != b
    assert a > b
    assert a >= b
    assert not a == b
    assert not a < b
    assert not a <= b
    print("Couple greater than test passed.")

    print("All tests passed.")


def main():
    '''Main function for the test.'''
    test_couple()

if __name__ == "__main__":
    main()

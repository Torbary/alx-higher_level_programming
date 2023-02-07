#!/usr/bin/python3
"""
    Module '100-my_int'
"""


class MyInt:
    """superclass"""


class MyInt(int):
    """subclass which inhierit int"""
    def __eq__(self, other):
        """retruns the negation"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """returns the opp of the result"""
        return not super().__ne__(other)

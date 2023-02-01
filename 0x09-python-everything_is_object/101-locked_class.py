#!/usr/bin/python3

"""Define a lockedClass"""


class LockedClass:
    """Prevent the user from instantiating new LockedClass
        attributes for anything but attributes called "firstname"
    """
    __slots__ = ["first_name"]

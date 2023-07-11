#!/usr/bin/python3
""" Student to JSON """


class Student:
    """ New class student """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return (self.__dict__)
        else:
            my_dict = {}
            for nm in attrs:
                if hasattr(self, nm):
                    my_dict[nm] = getattr(self, nm)
            return (my_dict)

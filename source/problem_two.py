"""
2) Write a new function with same functionality from Question 1, but it should be able to handle
a Python object in addition to a dictionary from Question 1.
Sample Input:
class Person(object):
def __init__(self, first_name, last_name, father):
self.first_name = first_name
self.last_name = last_name
self.father = father
person_a = Person(“User”, “1”, none)
person_b = Person(“User”, “2”, person_a)
a = {
“key1”: 1,
”key2”: {
“key3”: 1,
“key4”: {
“key5”: 4,
“user”: person_b,
}
},
}
Sample Output:
key1 1
key2 1
key3 2
key4 2
key5 3
user: 3
first_name: 4
last_name: 4
father: 4
first_name: 5
last_name: 5
father: 5
def print_depth(data):
# Write function body
You may write additional function.
"""

import sys


class Person(object):

    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


def print_depth(data, depth_value=1):
    if isinstance(data, Person):
        print(f"first_name {depth_value}")
        print(f"last_name {depth_value}")
        print(f"father {depth_value}")
        # print(data.first_name, depth_value)
        # print(data.last_name, depth_value)
        # print(data.father, depth_value)
        if isinstance(data.father, Person):
            print_depth(data.father, depth_value + 1)

    if isinstance(data, dict):
        for key, value in data.items():
            print(key, depth_value)
            if isinstance(value, object):
                print_depth(value, depth_value=depth_value + 1)


if __name__ == '__main__':
    person_a = Person("Mr X", "Khan", None)
    person_b = Person("Mr Y", "Rahman", person_a)
    a = {
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4,
                "user": person_b,
            }
        }
    }
    print_depth(a)

"""
1) Write the following function’s body. A nested dictionary is passed as parameter. You need to
print all keys with their depth.
Sample Input:
a = {
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4
            }
        }
    }

Sample Output:
key1 1
key2 1
key3 2
key4 2
key5 3
def print_depth(data):
# Write function body
You may write additional function.
"""

import sys


def print_depth(data, depth_value=1):
    for key, value in data.items():
        print(key, depth_value)
        if isinstance(value, dict):
            print_depth(value, depth_value=depth_value + 1)


if __name__ == '__main__':
    a = {
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4
            }
        }
    }
    print_depth(a)

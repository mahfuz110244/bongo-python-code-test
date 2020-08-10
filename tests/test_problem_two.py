from source.problem_two import Person, print_depth

person_a = Person("Mr X", "Khan", None)
person_b = Person("Mr Y", "Rahman", person_a)


def test_depth_level_empty(capsys):
    data = {
    }
    print_depth(data)
    captured = capsys.readouterr()
    assert captured.out == ""


def test_depth_level_one(capsys):
    data = {
        "key1": 1
    }
    print_depth(data)
    captured = capsys.readouterr()
    assert captured.out == (
            "key1 1\n"
        )


def test_depth_level_two(capsys):
    data = {
        "key1": 1,
        "key2": {
            "key3": 3
        }
    }
    print_depth(data)
    captured = capsys.readouterr()
    assert captured.out == (
            "key1 1\n"
            "key2 1\n"
            "key3 2\n"
        )


def test_depth_level_three(capsys):
    data = {
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4
            }
        }
    }
    print_depth(data)
    captured = capsys.readouterr()
    assert captured.out == (
            "key1 1\n"
            "key2 1\n"
            "key3 2\n"
            "key4 2\n"
            "key5 3\n"
        )


def test_depth_level_four_with_objects(capsys):
    data = {
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4,
                "user": person_a,
            }
        }
    }
    print_depth(data)
    captured = capsys.readouterr()
    assert captured.out == (
            "key1 1\n"
            "key2 1\n"
            "key3 2\n"
            "key4 2\n"
            "key5 3\n"
            "user 3\n"
            "first_name 4\n"
            "last_name 4\n"
            "father 4\n"
        )


def test_depth_level_five_with_objects(capsys):
    data = {
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4,
                "user": person_b,
            }
        }
    }
    print_depth(data)
    captured = capsys.readouterr()
    assert captured.out == (
            "key1 1\n"
            "key2 1\n"
            "key3 2\n"
            "key4 2\n"
            "key5 3\n"
            "user 3\n"
            "first_name 4\n"
            "last_name 4\n"
            "father 4\n"
            "first_name 5\n"
            "last_name 5\n"
            "father 5\n"
        )
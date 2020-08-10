from source.problem_one import print_depth


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
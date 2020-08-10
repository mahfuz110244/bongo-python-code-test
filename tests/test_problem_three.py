from source.problem_three import Node, lca

node1 = Node(1, None)
node2 = Node(2, node1)
node3 = Node(3, node1)
node4 = Node(4, node2)
node5 = Node(5, node2)
node6 = Node(6, node3)
node7 = Node(7, node3)
node8 = Node(8, node4)
node9 = Node(9, node4)


def test_root_node(capsys):
    lca(node1, node1)
    out, err = capsys.readouterr()
    assert out == "1\n"
    assert err == ""


def test_same_node(capsys):
    lca(node8, node8)
    out, err = capsys.readouterr()
    assert out == "8\n"
    assert err == ""


def test_child_node(capsys):
    lca(node2, node3)
    out, err = capsys.readouterr()
    assert out == "1\n"
    assert err == ""


def test_siblings_node(capsys):
    lca(node6, node7)
    out, err = capsys.readouterr()
    assert out == "3\n"
    assert err == ""


def test_leaf_node(capsys):
    lca(node8, node9)
    out, err = capsys.readouterr()
    assert out == "4\n"
    assert err == ""


def test_root_and_leaf_node(capsys):
    lca(node1, node9)
    out, err = capsys.readouterr()
    assert out == "1\n"
    assert err == ""


def test_root_chain_node(capsys):
    lca(node3, node7)
    out, err = capsys.readouterr()
    assert out == "3\n"
    assert err == ""
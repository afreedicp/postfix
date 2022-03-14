import postfixOperation


def testnonoperator():
    ret = postfixOperation.postfix_operator("1234")
    assert ret == [1, 2, 3, 4]

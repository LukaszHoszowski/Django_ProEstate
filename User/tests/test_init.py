import pytest


@pytest.mark.skip
def test_if_works():
    print('inside testcase')
    assert 10 == 10


@pytest.mark.skip
def test_if_works2(func):
    print('inside testcase2')
    assert 10 == func

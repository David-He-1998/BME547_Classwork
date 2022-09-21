import pytest


@pytest.mark.parametrize('Input, expect', [
        (85, 'Normal'),
        (59, 'Borderline Low'),
        (39, 'Low')])
def test_check_HDL(Input, expect):
    from Blood_Calculator import check_HDL
    ans = check_HDL(Input)
    assert ans == expect


@pytest.mark.parametrize('Input, expect', [
        (190, 'Very High'),
        (160, 'High'),
        (130, 'Borderline High'),
        (129, 'Normal')])
def test_check_LDL(Input, expect):
    from Blood_Calculator import check_LDL
    ans = check_LDL(Input)
    assert ans == expect

import pytest

@pytest.mark.parametrize('Input, expect',[(85,'Normal'),(59,'Borderline Low'),(39,'Low')])

def test_check_HDL(Input,expect):
    from Blood_Calculator import check_HDL
    ans=check_HDL(Input)
    assert ans==expect


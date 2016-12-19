#load the testing package
import pytest
from standard_deviation.standard_deviation import standard_deviation


#Below are the unit tests
# check if input is empty or not
def test_sd_nolength():
    with pytest.raises(ZeroDivisionError):
        assert standard_deviation([]), 'empty input should get ZeroDivisionError'

# Type error
def test_sd_string():
    with pytest.raises(TypeError):
        assert standard_deviation(["MDS"])


# check possitive numbers
def test_sd_positives():
    assert standard_deviation([1,1,1]) == 0


# Check negative number
def test_sd_negatives():
    assert standard_deviation([-1,-1,-1]) == 0

# Check all zero numbers
def test_sd_negatives():
    assert standard_deviation([0,0,0]) == 0

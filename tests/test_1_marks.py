from hanoi.basics import Position, number_of_positions, number_of_steps_of_solution
import pytest


# -- Exercise 1* --
# How many positions does the Tower of Hanoi have for n disks? Implement your answer in number_of_positions() in
# hanoi/basics.py and make sure the following test passes.
def test_number_of_positions() -> None:
    number_of_disks = 1
    result = number_of_positions(number_of_disks=number_of_disks)
    expected_result = 3
    assert result == expected_result


# -- Exercise 2 --
# Write a test to find out what happens if you implement two tests with the same name.


# -- Exercise 3 --
# Write a test to find out whether code after the assert-line is executed.
# Does this depend on the outcome of the assertion?


# -- Exercise 4* --
# Implement number_of_steps_of_solution() in hanoi/basics.py, which returns the number of steps it takes to solve the
# Tower of Hanoi with n disks. Write a test with multiple asserts, that checks if your implementation is correct if the
# number of disks is 1, 2 or 3.

@pytest.mark.parametrize(("input","expected"), [(1,1),(2,3),(3,7)])
def test_number_of_steps(input, expected) -> None:
    assert number_of_steps_of_solution(input) == expected
    


# -- Exercise 5 --
# Write a test that checks whether the solution for 1000 disks takes more than 1000 steps. But use marks to skip it if
# the number of available cpus is less than 32.


# -- Exercise 6* --
# If you call number_of_steps_of_solution() with a string as input, it probably raises an error. For now, we don't know
# how to handle this properly, so mark the test as a failure.
def test_wrong_input() -> None:
    number_of_steps_of_solution(number_of_disks="12")  # type: ignore


# -- Exercise 7 --
# The following test, raises a warning. Because we purposely want to test a long position, let pytest ignore the warning
# using pytest.marks.filterwarnings (https://docs.pytest.org/en/6.2.x/reference.html#pytest-mark-filterwarnings)
def test_long_position() -> None:
    Position(101 * "a")


# -- Exercise 8 --
# According to a legend, the biggest version of this puzzle is situated in the Kashi Vishwanath Temple in India.
# Priests have started moving around the 64 golden disks in 1780 and once they are finished the earth will vanish.
# Write a test that warns us (so let the test fail) if the priests will finish within 100 years from now. Assume the
# priests can move 1 disk per second.

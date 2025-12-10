import pytest
from dsa_lib.strings import fizzbuzz  # Import the function

# --------------------------------Start FizzBuzz---------------------------------------------


@pytest.mark.parametrize(
    "n, expected_list",
    [
        # Case 1: Simple case, stops before Fizz
        (1, ["1"]),
        # Case 2: Stops exactly at first Fizz
        (3, ["1", "2", "Fizz"]),
        # Case 3: Includes Fizz and Buzz
        (5, ["1", "2", "Fizz", "4", "Buzz"]),
        # Case 4: Standard sequence up to 15 (FizzBuzz)
        (
            15,
            [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "FizzBuzz",
            ],
        ),
    ],
)
def test_fizzbuzz_sequence(n, expected_list):
    """
    Verifies that fizzbuzz(n) returns the correct list sequence from 1 to n.
    """
    # Assuming your function is named fizzbuzz and takes 'n'
    assert fizzbuzz(n) == expected_list


def test_fizzbuzz_empty():
    """
    Edge case: If input is 0, should return empty list (since range is 1 to n).
    """
    assert fizzbuzz(0) == []


def test_fizzbuzz_large_input_length():
    """
    Performance/Logic check: Ensure the list length matches n.
    """
    result = fizzbuzz(100)
    assert len(result) == 100
    assert result[99] == "Buzz"  # 100th element (index 99) should be Buzz


# ------------------------------End FizzBuzz---------------------------------------------

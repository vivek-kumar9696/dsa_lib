import pytest
from dsa_lib.strings import (
    fizzbuzz,
    longest_common_prefix,
    encode_string,
    decode_string,
)  # Import the function

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


# -------------------------------Start Longest Common Prefix--------------------------------
@pytest.mark.parametrize(
    "strs, expected",
    [
        # Case 1: Standard common prefix
        (["flower", "flow", "flight"], "fl"),
        # Case 2: No common prefix exists
        (["dog", "racecar", "car"], ""),
        # Case 3: All strings are identical
        (["testing", "testing", "testing"], "testing"),
        # Case 4: One string is a prefix of another
        (["ab", "abc", "abcd"], "ab"),
        # Case 5: List contains an empty string (result should be empty)
        (["flower", "flow", ""], ""),
        # Case 6: Single character match
        (["a", "ac"], "a"),
        # Case 7: Very short strings matching
        (["c", "c"], "c"),
    ],
)
def test_longest_common_prefix_standard(strs, expected):
    """
    Tests standard scenarios including matches, no matches, and partial matches.
    """
    assert longest_common_prefix(strs) == expected


def test_lcp_empty_list():
    """
    Edge Case: The input list is empty. Should return an empty string.
    """
    assert longest_common_prefix([]) == ""


def test_lcp_single_string():
    """
    Edge Case: The list contains only one string. The prefix is the string itself.
    """
    assert longest_common_prefix(["single"]) == "single"


def test_lcp_first_char_mismatch():
    """
    Specific check: If the very first characters differ, return empty string immediately.
    """
    strs = ["apple", "banana", "pear"]
    assert longest_common_prefix(strs) == ""


# ----------------------------------End Longest Common Prefix----------------------------------------

# --------------------------------------Start Encode Decode String--------------------------------------


@pytest.mark.parametrize(
    "original_list",
    [
        # Case 1: Simple words
        (["hello", "world"]),
        # Case 2: Single word
        (["algorithm"]),
        # Case 3: Empty string in the list
        (["", "test", ""]),
        # Case 4: Special characters and numbers
        (["#", "123", " "]),
        # Case 5: Empty list
        ([]),
        # Case 6: Strings with maximum supported length (15 chars for 4-bit header)
        (["a" * 15, "b" * 5]),
    ],
)
def test_encode_decode_logic(original_list):
    """
    Verifies that decoding the encoded string returns exactly the original list.
    """
    encoded = encode_string(original_list)
    decoded = decode_string(encoded)
    assert decoded == original_list

    # ------------------------End Encode Decode String---------------------

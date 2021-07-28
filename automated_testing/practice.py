import pytest

def count_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    total = 0
    word = list(string.lower())
    for vowel in vowels:
        if vowel in word:
            total += 1
    return total

print(count_vowels("Matt"))

def test_vowel_count():
    assert count_vowels("Matt") == 1


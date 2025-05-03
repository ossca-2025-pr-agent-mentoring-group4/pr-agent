def sort_even_numbers(numbers):
    """
    짝수만 필터링하여 오름차순으로 정렬합니다.
    예시 입력: [5, 2, 8, 1]
    예시 출력: [2, 8]
    """
    even_numbers = [num for num in numbers if num % 2 == 0]
    return sorted(even_numbers)


def is_prime(n):
    """
    소수(prime number) 여부를 판단합니다.
    예시 입력: 7 → 출력: True / 8 → 출력: False
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def test_sort_even_numbers():
    """
    Test: sort_even_numbers 함수의 정렬 결과가 올바른지 검증합니다.
    """
    sample = [10, 1, 4, 3, 8]
    expected = [4, 8, 10]
    result = sort_even_numbers(sample)
    assert result == expected, f"Expected {expected}, but got {result}"


def test_is_prime():
    """
    Test: is_prime 함수의 소수 판별이 정확한지 확인합니다.
    """
    assert is_prime(2) == True
    assert is_prime(9) == False
    assert is_prime(17) == True

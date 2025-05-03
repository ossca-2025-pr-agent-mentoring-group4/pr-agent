def test_behavior():
    """
    주어진 숫자 리스트에서 짝수만 필터링한 후 정렬하여 반환합니다.
    테스트와 리뷰 대상 확인을 위해 작성된 함수입니다.
    """
    numbers = [10, 3, 4, 15, 2, 7, 8]
    even_numbers = [num for num in numbers if num % 2 == 0]
    sorted_evens = sorted(even_numbers)
    return sorted_evens


def new_feature():
    """
    입력된 문자열이 회문(palindrome)인지 여부를 판별합니다.
    예: 'level', 'madam'은 회문입니다.
    """
    test_strings = ["level", "robot", "madam", "python"]
    results = {}
    for s in test_strings:
        is_palindrome = s == s[::-1]
        results[s] = is_palindrome
        print(f"{s}: {'Palindrome' if is_palindrome else 'Not a palindrome'}")
    return results
def is_palindrome(text: str) -> bool:
    return text == text[::-1]


def is_almost_palindrome(text: str) -> bool:
    for i in range(len(text)):
        if is_palindrome(text[:i] + text[i + 1:]):
            return True
    return False


s: str = input()
if not is_palindrome(s):
    print("YES" if is_almost_palindrome(s) else "NO")
else:
    print("YES")

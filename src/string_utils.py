class StringUtils:
    @staticmethod
    def reverse(text: str) -> str:
        return text[::-1]

    @staticmethod
    def is_palindrome(text: str) -> bool:
        normalized = text.lower().replace(" ", "")
        return normalized == normalized[::-1]

    @staticmethod
    def count_vowels(text: str) -> int:
        vowels = "aeiou"
        return sum(1 for char in text.lower() if char in vowels)

    @staticmethod
    def to_title_case(text: str) -> str:
        return text.title()

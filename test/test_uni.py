import pytest


class TestNameValidations:

    def test_valid_names(self, valid_name):
        assert valid_name("David X. C.")
        assert valid_name("David Michael Fair")
        assert valid_name("David D. Michael")
        assert valid_name("John Doe")

    def test_invalid_names(self, valid_name):
        assert isinstance(valid_name("David"), ValueError)  # только одно слово
        assert isinstance(valid_name("X. C."), ValueError)  # недостаточно заглавных слов
        assert isinstance(valid_name("David x. C."), ValueError)  # некорректный формат
        assert isinstance(valid_name("david Michael"), ValueError)  # первая буква должна быть заглавной

    def test_edge_cases(self, valid_name):
        assert isinstance(valid_name("A B"), ValueError)  # минимально допустимые два слова
        assert isinstance(valid_name("A B C"), ValueError)  # корректное, но с недостатком формата
        assert isinstance(valid_name("  David Michael  "), ValueError)  # лишние пробелы не должны влиять


class TestUrlValidations:
 

    def test_valid_url(self, valid_url):
        # Тестируем допустимые URL
        assert valid_url("https://example.com")
        assert valid_url("https://www.google.com")
        assert valid_url("https://subdomain.example.com")

    def test_invalid_url_missing_https(self, valid_url):
        # Недопустимые URL без https://
        assert isinstance(valid_url("http://example.com"), ValueError)
        assert isinstance(valid_url("ftp://example.com"), ValueError)
        assert isinstance(valid_url("www.example.com"), ValueError)

    def test_invalid_url_special_characters(self, valid_url):
        # Недопустимые URL с неправильными символами
        assert isinstance(valid_url("https://example.com/<>"), ValueError)
        assert isinstance(valid_url("https://example.com/#invalid"), ValueError)

    def test_invalid_url_empty_string(self, valid_url):
        # Пустая строка как URL
        assert isinstance(valid_url(""), ValueError)

    def test_invalid_url_partial_https(self, valid_url):
        # Частично корректный URL (например, начинается с https, но не полон)
        assert isinstance(valid_url("https:"), ValueError)
        assert isinstance(valid_url("https://"), ValueError)

class TestUrlValidations2:
    def test_valid_url_2(self, valid_url_2):
        # Тестируем допустимые URL
        assert valid_url_2("https://example.com")
        assert valid_url_2("https://www.google.com")
        assert valid_url_2("https://demoqa.com/")

    def test_invalid_url_2_missing_https(self, valid_url_2):
        # Недопустимые URL без https://
        assert isinstance(valid_url_2("ftp://example.com"), ValueError)
        assert isinstance(valid_url_2("www.example.com"), ValueError)


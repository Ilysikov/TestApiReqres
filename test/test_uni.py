from models.questions import ValidFuturama
import pytest


class TestNameValidations:

    def test_valid_names(self):
        assert ValidFuturama.valid_name("David X. C.")
        assert ValidFuturama.valid_name("David Michael Fair")
        assert ValidFuturama.valid_name("David D. Michael")
        assert ValidFuturama.valid_name("John Doe")

    def test_invalid_names(self):
        assert isinstance(ValidFuturama.valid_name("David"), ValueError)  # только одно слово
        assert isinstance(ValidFuturama.valid_name("X. C."), ValueError)  # недостаточно заглавных слов
        assert isinstance(ValidFuturama.valid_name("David x. C."), ValueError)  # некорректный формат
        assert isinstance(ValidFuturama.valid_name("david Michael"), ValueError)  # первая буква должна быть заглавной

    def test_edge_cases(self):
        assert isinstance(ValidFuturama.valid_name("A B"), ValueError)  # минимально допустимые два слова
        assert isinstance(ValidFuturama.valid_name("A B C"), ValueError)  # корректное, но с недостатком формата
        assert isinstance(ValidFuturama.valid_name("  David Michael  "), ValueError)  # лишние пробелы не должны влиять


class TestUrlValidations:
 

    def test_valid_url(self):
        # Тестируем допустимые URL
        assert ValidFuturama.valid_url("https://example.com")
        assert ValidFuturama.valid_url("https://www.google.com")
        assert ValidFuturama.valid_url("https://subdomain.example.com")

    def test_invalid_url_missing_https(self):
        # Недопустимые URL без https://
        assert isinstance(ValidFuturama.valid_url("http://example.com"), ValueError)
        assert isinstance(ValidFuturama.valid_url("ftp://example.com"), ValueError)
        assert isinstance(ValidFuturama.valid_url("www.example.com"), ValueError)

    def test_invalid_url_special_characters(self):
        # Недопустимые URL с неправильными символами
        assert isinstance(ValidFuturama.valid_url("https://example.com/<>"), ValueError)
        assert isinstance(ValidFuturama.valid_url("https://example.com/#invalid"), ValueError)

    def test_invalid_url_empty_string(self):
        # Пустая строка как URL
        assert isinstance(ValidFuturama.valid_url(""), ValueError)

    def test_invalid_url_partial_https(self):
        # Частично корректный URL (например, начинается с https, но не полон)
        assert isinstance(ValidFuturama.valid_url("https:"), ValueError)
        assert isinstance(ValidFuturama.valid_url("https://"), ValueError)

class TestUrlValidations2:
    def test_valid_url_2(self):
        # Тестируем допустимые URL
        assert ValidFuturama.valid_url_2("https://example.com")
        assert ValidFuturama.valid_url_2("https://www.google.com")
        assert ValidFuturama.valid_url_2("https://demoqa.com/")

    def test_invalid_url_2_missing_https(self):
        # Недопустимые URL без https://
        assert isinstance(ValidFuturama.valid_url_2("ftp://example.com"), ValueError)
        assert isinstance(ValidFuturama.valid_url_2("www.example.com"), ValueError)


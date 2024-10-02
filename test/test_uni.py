import unittest
from models.questions import ValidFuturama


class TestNameValidation(unittest.TestCase):

    def test_valid_names(self):
        self.assertTrue(ValidFuturama.valid_name("David X. C."))
        self.assertTrue(ValidFuturama.valid_name("David Michael Fair"))
        self.assertTrue(ValidFuturama.valid_name("David D. Michael"))
        self.assertTrue(ValidFuturama.valid_name("John Doe"))

    def test_invalid_names(self):
        self.assertTrue(ValidFuturama.valid_name("David"), ValueError(str))  # только одно слово
        self.assertTrue(ValidFuturama.valid_name("X. C."), ValueError(str))  # недостаточно заглавных слов
        self.assertTrue(ValidFuturama.valid_name("David x. C."), ValueError(str))  # некорректный формат
        self.assertTrue(ValidFuturama.valid_name("david Michael"), ValueError(str))  # первая буква должна быть заглавной

    def test_edge_cases(self):
        self.assertTrue(ValidFuturama.valid_name("A B"), ValueError(str))  # минимально допустимые два слова
        self.assertTrue(ValidFuturama.valid_name("A B C"), ValueError(str))  # корректное, но с недостатком формата
        self.assertTrue(ValidFuturama.valid_name("  David Michael  "), ValueError(str))  # лишние пробелы не должны влиять


if __name__ == "__main__":
    unittest.main()

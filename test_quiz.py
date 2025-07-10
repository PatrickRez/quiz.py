import unittest
from unittest import mock
from io import StringIO
from quiz import quiz, show_question, get_answer, check_answer

class TestQuiz(unittest.TestCase):
    def test_get_answer_valid(self):
        question = quiz[0]
        # Simula o usuário digitando '1' (primeira opção: Paris)
        with mock.patch('builtins.input', return_value='1'):
            answer = get_answer(question)
        self.assertEqual(answer, question["options"][0])

    def test_get_answer_invalid(self):
        question = quiz[1]
        # Simula o usuário digitando '2' (segunda opção: Pequim)
        with mock.patch('builtins.input', return_value='2'):
            answer = get_answer(question)
        # A resposta correta é "Tóquio" (primeira opção), então deve ser diferente
        self.assertNotEqual(answer, question["answer"])

    def test_check_answer_correct(self):
        question = quiz[0]
        user_answer = question["options"][0]
        self.assertTrue(check_answer(user_answer, question["answer"]))

    def test_check_answer_incorrect(self):
        question = quiz[0]
        user_answer = "Resposta Incorreta"
        self.assertFalse(check_answer(user_answer, question["answer"]))

    def test_show_question(self):
        question = quiz[0]
        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            show_question(question)
            output = fake_out.getvalue()
        self.assertIn(question["question"], output)
        for option in question["options"]:
            self.assertIn(option, output)

if __name__ == "__main__":
    unittest.main()
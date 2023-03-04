import unittest
from unittest.mock import patch

import pytest
from Quiz.quiz import play_game, QUESTIONS_AND_ANSWERS


class PlayQuizTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    @patch('Quiz.quiz.get_input', side_effect=["Guido van Rossum", "bool", "94", "1991", "="])
    def test_all_correct_answers(self, input):
        actual_result = play_game(QUESTIONS_AND_ANSWERS)
        expected_result = 5
        self.assertEqual(expected_result, actual_result)

    @pytest.mark.task(taskno=2)
    @patch('Quiz.quiz.get_input', side_effect=["Guido van Rossum", "bool", "94", "1991", "=="])
    def test_4_correct_answers(self, input):
        actual_result = play_game(QUESTIONS_AND_ANSWERS)
        expected_result = 4
        self.assertEqual(expected_result, actual_result)

    @pytest.mark.task(taskno=3)
    @patch('Quiz.quiz.get_input', side_effect=["Guido van Rossum", "bool", "", "199", "=="])
    def test_2_correct_answers(self, input):
        actual_result = play_game(QUESTIONS_AND_ANSWERS)
        expected_result = 2
        self.assertEqual(expected_result, actual_result)

    @pytest.mark.task(taskno=4)
    @patch('Quiz.quiz.get_input', side_effect=["Guido ", "ool", "", "199", "=="])
    def test_no_correct_answers(self, input):
        actual_result = play_game(QUESTIONS_AND_ANSWERS)
        expected_result = 0
        self.assertEqual(expected_result, actual_result)

import unittest

from unittest import TestCase

import task_1_secretary, task_1_vote, task_1_quadratic_equation

class TestSecretaryName(TestCase):
    def test_task_secretary_there_is_a_document(self):
        name_doc = "10006"
        expected = "Аристарх Павлов"

        result = task_1_secretary.get_name(name_doc)

        self.assertEqual(expected, result)


    def test_task_secretary_no_document(self):
        name_doc = "101"
        expected = 'Документ не найден'

        result = task_1_secretary.get_name(name_doc)

        self.assertEqual(expected, result)


    def test_task_secretary(self):
        for i, (name_doc, expected) in enumerate([
            ("10006", "Аристарх Павлов"),
            # ('311 020203', 'Александр Пушкин'),
            ("101", 'Документ не найден'),

        ]):
            with self.subTest(i):
                result = task_1_secretary.get_name(name_doc)
                self.assertEqual(expected, result)


    def test_task_secretary_get_directory(self):
        for i, (doc_number, expected) in enumerate([
            ("11-2", '1'),
            ('311', 'Полки с таким документом не найдено'),

        ]):
            with self.subTest(i):
                result = task_1_secretary.get_directory(doc_number)
                self.assertEqual(expected, result)



    def test_kask_vote(self):
        for i, (voice, expected) in enumerate([
            ([1, 1, 1, 2, 3], 1),
            ([1, 2, 3, 2, 2], 2),

        ]):
            with self.subTest(i):
                result = task_1_vote.vote(voice)
                self.assertEqual(expected, result)



    def test_task_quadratic_equation(self):
        for i, (a, b, c, expected) in enumerate([
            (1, 8, 15, (-3.0, -5.0)),
            (1, -13, 12, (12.0, 1.0)),
            (-4, 28, -49, 3.5),
            (1, 1, 1, 'корней нет'),
        ]):
            with self.subTest(i):
                result = task_1_quadratic_equation.solution(a, b, c)
                print('---', result)
                self.assertEqual(expected, result)
import pytest

import task_1_secretary, task_1_vote, task_1_quadratic_equation


def test_task_secretary_there_is_a_document():
    name_doc = "10006"
    expected = "Аристарх Павлов"

    result = task_1_secretary.get_name(name_doc)

    assert expected == result


def test_task_secretary_no_document():
    name_doc = "101"
    expected = 'Документ не найден'

    result = task_1_secretary.get_name(name_doc)

    assert expected == result

@pytest.mark.parametrize(
    'name_doc, expected',
    (
        ["10006", "Аристарх Павлов"],
        # ['311 020203', 'Александр Пушкин'],
        ["101", 'Документ не найден'],
    )
)
def test_task_secretary(name_doc, expected):
    result = task_1_secretary.get_name(name_doc)
    assert result == expected


@pytest.mark.parametrize(
    'doc_number, expected',
    (
        ["11-2", '1'],
        ['311', 'Полки с таким документом не найдено'],
    )
)
def test_task_secretary_get_directory(doc_number, expected):
    result = task_1_secretary.get_directory(doc_number)
    assert result == expected


# # ----------------------------------------------
@pytest.mark.parametrize(
    'voice, expected',
    (
        [[1, 1, 1, 2, 3], 1],
        [[1, 2, 3, 2, 2], 2],
    )
)
def test_task_vote(voice, expected):
    result = task_1_vote.vote(voice)
    assert result == expected


# # --------------------------------------------
@pytest.mark.parametrize(
    'a, b, c, expected',
    (
        [1, 8, 15, (-3.0, -5.0)],
        [1, -13, 12, (12.0, 1.0)],
        [-4, 28, -49, 3.5],
        [1, 1, 1, 'корней нет'],
    )
)
def test_task_quadratic_equation(a, b, c, expected):
    result = task_1_quadratic_equation.solution(a, b, c)
    assert result == expected
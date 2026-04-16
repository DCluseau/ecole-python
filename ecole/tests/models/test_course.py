# -*- coding: utf-8 -*-

"""
Course class tests
"""
import pytest

from datetime import date

from ecole.models.course import Course
from ecole.models.teacher import Teacher
from ecole.models.student import Student

def test_should_set_teacher():
    expected_value = Teacher("Martial", "Bret", 50, date(2018,9, 1))
    sut = Course("Python", date(2025, 9, 22), date(2026, 4, 10))
    sut.set_teacher(expected_value)
    assert sut.teacher == expected_value

def test_should_set_student():
    expected_value = Student("Daphné", "Cluseau", 38)
    sut = Course("Python", date(2025, 9, 22), date(2026, 4, 10))
    sut.add_student(expected_value)
    assert sut.students_taking_it[0] == expected_value

def test_should_return_name_dates_teacher():
    teacher = Teacher("Martial", "Bret", 50, date(2018, 9, 1))
    sut = Course("Python", date(2025, 9, 22), date(2026, 4, 10))
    sut.set_teacher(teacher)
    expected_value = f"Python (2025-09-22 – 2026-04-10),\nenseigné par {teacher}"
    assert sut.__str__() == expected_value
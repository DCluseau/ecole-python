# -*- coding: utf-8 -*-

"""
Course class tests
"""
import pytest

from datetime import date

from ecole.models.course import Course
from ecole.models.teacher import Teacher

def test_should_set_teacher():
    expected_value = Teacher("Martial", "Bret", 50, date(2018,9, 1))
    sut = Course("Python", date(2025, 9, 22), date(2026, 4, 10))
    sut.set_teacher(expected_value)
    assert sut.teacher == expected_value

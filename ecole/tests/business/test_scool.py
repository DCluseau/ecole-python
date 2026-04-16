# -*- coding: utf-8 -*-

"""
Course class tests
"""
import pytest

from datetime import date

from ecole.business.school import School
from ecole.models.course import Course

def test_should_add_course():
    sut = School()
    course = Course("Python", date(2025, 9, 22), date(2026, 4, 10))
    sut.add_course(course)
    expected_value = course
    assert sut.courses[len(sut.courses) - 1] == expected_value
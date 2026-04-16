# -*- coding: utf-8 -*-

"""
Course class tests
"""
import pytest

from datetime import date

from ecole.models.course import Course
from ecole.models.teacher import Teacher
from ecole.models.student import Student

def test_should_add_course_to_teacher_course_list():
    sut = Teacher("Martial", "Bret", 50, date(2018, 9, 1))
    course = Course("Python", date(2025, 9, 22), date(2026, 4, 10))
    expected_value = [course]
    sut.add_course(course)
    assert sut.courses_teached == expected_value


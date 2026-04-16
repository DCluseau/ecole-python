# -*- coding: utf-8 -*-

"""
Student class tests
"""
import pytest

from datetime import date

from ecole.models.course import Course
from ecole.models.student import Student

def test_should_add_one_to_nb_of_created_students():
    expected_value = 1
    student = Student("Daphné", "Cluseau", 38)
    assert student.students_nb == expected_value

def test_should_add_course_to_student():
    sut = Student("Daphné", "Cluseau", 38)
    course = Course("Python", date(2025, 9, 22), date(2026, 4, 10))
    sut.add_course(course)
    expected_value = course
    assert sut.courses_taken[0] == expected_value

def test_should_display_student():
    """
    nb_student is expected to be 3 because of the two previous tests which each created a student
    This test allows to test __str__ method of Person abstract class too
    """
    expected_value = "Daphné Cluseau (38 ans), n° étudiant : 3"
    sut = Student("Daphné", "Cluseau", 38)
    assert sut.__str__() == expected_value
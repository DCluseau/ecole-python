# -*- coding: utf-8 -*-

"""
Course class tests
"""
import pytest

from datetime import date

from ecole.business.school import School
from ecole.models.course import Course
from ecole.models.student import Student
from ecole.models.teacher import Teacher


def test_should_add_course():
    sut = School()
    course = Course("Python", date(2025, 9, 22), date(2026, 4, 10))
    sut.add_course(course)
    expected_value = course
    assert sut.courses[0] == expected_value

def test_should_add_teacher():
    sut = School()
    teacher = Teacher("Martial", "Bret", 50, date(2018,9, 1))
    sut.add_teacher(teacher)
    expected_value = teacher
    assert sut.teachers[0] == expected_value

def test_should_add_student():
    sut = School()
    student = Student("Daphné", "Cluseau", 38)
    sut.add_student(student)
    expected_value = student
    assert sut.students[0] == expected_value

def test_should_have_correct_nb_of_courses():
    sut = School()
    sut.init_static()
    expected_value = 8
    assert len(sut.courses) == expected_value

def test_should_have_correct_nb_of_students():
    sut = School()
    sut.init_static()
    expected_value = 3
    assert len(sut.students) == expected_value

def test_should_have_correct_nb_of_teachers():
    sut = School()
    sut.init_static()
    expected_value = 6
    assert len(sut.teachers) == expected_value
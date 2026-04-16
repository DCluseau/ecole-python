# -*- coding: utf-8 -*-

"""
Address class tests
"""
import pytest

from ecole.models.address import Address

def test_str_should_display_object():
    sut = Address("chemin de la Butte", "Toulouse", 31400)
    expected_value = "chemin de la Butte, 31400 Toulouse"
    assert sut.__str__() == expected_value

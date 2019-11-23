""" Priority Tests

Test conversions between Todoist and Taskwarrior priorities.
"""
import pytest
from todoist_taskwarrior import utils


def test_priorities():
    assert utils.ti_priority_to_tw(1) == None
    assert utils.ti_priority_to_tw(2) == 'L'
    assert utils.ti_priority_to_tw(3) == 'M'
    assert utils.ti_priority_to_tw(4) == 'H'

def test_priorities_str():
    assert utils.ti_priority_to_tw('1') == None
    assert utils.ti_priority_to_tw('2') == 'L'
    assert utils.ti_priority_to_tw('3') == 'M'
    assert utils.ti_priority_to_tw('4') == 'H'


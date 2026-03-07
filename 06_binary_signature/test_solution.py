import os
import json
import pytest

def test_task():
    with open('type.txt') as f: assert f.read().strip() == 'PNG'
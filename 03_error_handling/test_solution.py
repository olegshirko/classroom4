import os
import json
import pytest

def test_task():
    with open('log.txt') as f: assert 'ERROR' in f.read()
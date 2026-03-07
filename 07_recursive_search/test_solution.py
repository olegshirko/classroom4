import os
import json
import pytest

def test_task():
    with open('found.txt') as f: 
        content = f.read()
        assert 'a.txt' in content and 'b.txt' in content and 'c.py' not in content
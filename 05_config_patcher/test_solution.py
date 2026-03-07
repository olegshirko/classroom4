import os
import json
import pytest

def test_task():
    with open('config.env') as f: 
        lines = f.readlines()
        assert 'DEBUG=True\n' in lines or 'DEBUG=True' in lines
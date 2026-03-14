import os
import json
import pytest

def test_task():
    with open('output.txt') as f: assert f.read().strip() == '2,4,6,10'
import os
import json
import pytest

import json
def test_task():
    with open('users.json') as f: 
        d = json.load(f)
        assert d[0]['id'] == '1' and d[1]['name'] == 'Maria'
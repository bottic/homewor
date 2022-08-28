import pytest
from work_test.main import add_new_file_in_disk
from pathlib import Path

file_to_add = 'set.py'
DICT_PATH = Path.cwd()
full_path = Path(DICT_PATH, file_to_add)

fixture = [
    ('set.py', full_path, 'AQAAAAAvvfGKAADLW5uYtnIKaU9AnB5KfrYe1kQ', 201)
]

@pytest.mark.parametrize('file_name_in_disk, file_path, token, result', fixture)
def test_add_new_file_disk(file_name_in_disk, file_path, token, result):
    calc_res = add_new_file_in_disk(file_name_in_disk, file_path, token)
    assert calc_res == result



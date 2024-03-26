import pytest
import os
from app.main import write_output
import csv
from io import StringIO


@pytest.fixture
def output_file(tmpdir):
    file_path = os.path.join(tmpdir, 'output.csv')
    print(f"Temporary file path: {file_path}")
    return file_path


def test_write_output_single_entry(output_file):
    symbol_stats = [('aaa', 1000, 45, 25, 30)]
    write_output(output_file, symbol_stats)

    # Reading temporary output file
    with open(output_file, 'r') as file:
        reader = csv.reader(file)
        row = next(reader)
        assert row == ['aaa', '1000', '45', '25', '30']

import pytest
from app.main import write_output
import csv


@pytest.fixture
def output_file(tmp_path):
    file_path = tmp_path / 'output.csv'
    print(f"Temporary file path: {file_path}")
    return file_path


def test_write_output_single_entry(output_file):
    symbol_stats = [('aaa', 1000, 45, 25, 30)]
    write_output(output_file, symbol_stats)

    # Reading temporary output file
    with open(output_file, 'r') as file:
        row = next(csv.reader(file))
        assert row == ['aaa', '1000', '45', '25', '30']

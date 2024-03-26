import pytest

from app.main import process_trades, calculate_stats, write_output
import csv
import os


@pytest.fixture
def input_file_path():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(root_dir, '..', 'input.csv')
    return input_file


@pytest.fixture
def expected_output_file_path():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(root_dir, '..', 'app', 'output.csv')
    return output_file


def test_final_result(input_file_path, expected_output_file_path, tmp_path):
    trades_by_symbol = process_trades(input_file_path)
    symbol_stats = calculate_stats(trades_by_symbol)

    # Writing output to temp file
    output_file_path = tmp_path / 'output.csv'
    write_output(output_file_path, symbol_stats)

    assert_files_equal(output_file_path, expected_output_file_path)


def assert_files_equal(file_path1, file_path2):
    # Comparing both files
    with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
        file1_contents = list(csv.reader(file1))
        file2_contents = list(csv.reader(file2))
        assert file1_contents == file2_contents

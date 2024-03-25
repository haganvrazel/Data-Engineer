from app.main import process_trades
import os
import pytest

input_file = 'test_input.csv'

test_data = [
    ("1234567,aaa,10,12\n"
     "1234568,aaa,20,15\n"
     "1234569,bbb,15,18\n")
]


@pytest.fixture(scope='module')
def initialize_input_file():
    with open(input_file, 'w') as file:
        file.writelines(test_data)
    yield
    os.remove(input_file)


# test cases
def test_process_trades(initialize_input_file):
    expected_output = {
        'aaa': [(1234567, 10, 12), (1234568, 20, 15)],
        'bbb': [(1234569, 15, 18)]
    }
    actual_output = process_trades(input_file)

    # debugging purposes
    print("Expected output: ", expected_output)
    print("Actual output: ", actual_output)

    assert actual_output == expected_output


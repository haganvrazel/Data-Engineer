from app.main import calculate_stats


def test_calculate_stats_single_symbol():
    trades_by_symbol = {
        'aaa': [(1000, 10, 20), (2000, 15, 25), (3000, 20, 30)]
    }
    expected_output = [('aaa', 1000, 45, 26, 30)]
    assert calculate_stats(trades_by_symbol) == expected_output


def test_calculate_stats_single_trade():
    trades_by_symbol = {
        'aaa': [(1000, 10, 20)]
    }
    expected_output = [('aaa', 0, 10, 20, 20)]
    assert calculate_stats(trades_by_symbol) == expected_output


def test_calculate_stats_complex():
    trades_by_symbol = {
        'aaa': [(1000, 10, 12), (2000, 20, 15), (3000, 30, 18)],
        'bbb': [(4000, 5, 20), (6000, 10, 25), (7000, 15, 30)],
        'ccc': [(8000, 7, 22), (9000, 8, 24)]
    }
    expected_output = [
        ('aaa', 1000, 60, 16, 18),
        ('bbb', 2000, 30, 26, 30),
        ('ccc', 1000, 15, 23, 24)
    ]
    assert calculate_stats(trades_by_symbol) == expected_output


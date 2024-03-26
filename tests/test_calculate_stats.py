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


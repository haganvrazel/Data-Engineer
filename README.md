### Quantlab Trading Project

Ensure input.csv is located in the root directory of your project when testing.

```bash
pip install pytest
```

### Approach Overview

The project implements a trading data processing system that reads trade data from an input CSV file, calculates various statistics for each symbol, and writes the results to an output CSV file. The logic is split into three main functions: reading trade data from a file, calculating statistics for each symbol, and writing the results to an output file.

### Key Components:

   ```python
1. process_trades(input_file):
   ```
   - Reads trade data from the input CSV file and organizes it into a dictionary where each symbol maps to a list of trades.
   - Utilizes Python's csv library to parse the CSV file efficiently.
   - Uses defaultdict(list) for intuitive data structuring.

   ```python
2. calculate_stats(trades_by_symbol):
   ```
   - Computes various statistics for each symbol based on the trade data.
   - Calculates metrics such as the maximum time gap, total volume, weighted average price, and maximum price.
   - Implements sorting by symbol ascending to maintain consistency.

   ```python
3. write_output(output_file, symbol_stats):
   ```
   - Writes the computed statistics for each symbol to the output CSV file.
   - Sorts the data by symbol as per requirement.
### Explanation:

- Modular Design: The project is structured into modular functions to have separation of concerns, enabling easier testing, debugging, and maintenance.
- Readability: Organization of code and variables follows the flow of natural English language resulting variable having a self-explanatory description.
- Efficiency: Utilizes Python's built-in libraries (csv, defaultdict) for efficient file handling and data structuring.
- Testing: Implements unit tests using pytest to ensure the correctness of individual components and overall functionality.

Note: Used @pytest.fixture for code reusability and resource management.


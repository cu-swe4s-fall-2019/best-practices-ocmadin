# Best Practices Testing

## Contents

### `style.py`
`style.py` contains examples of proper styling for a variety of python functions

### `get_column_stats.py`
`get_column_stats.py` contains a function for extracting the mean and standard deviation from a specified column of an input file

### `basics_test.sh`
`basics_test.sh` contains functional tests for `get_column_stats.py`.  This includes tests to ensure pep8 compliance, as well as input and output tests for the function.

### `basics_test.py`
`basics_test.py` contains unit tests for the `calculate_mean` and `calculate_stdev` methods within `get_column_stats.py`.  These tests check for things like correct inputs, as well as ensuring that the functions calculate correctly.

## Usage

To calculate the stats of a column in a file, use `python get_column_stats.py -f <filename> -c <column number>`

To run the bash functional tests, use ` . basics_test.sh`

To run the python unit tests, use `python -m unittest basics_test.py`

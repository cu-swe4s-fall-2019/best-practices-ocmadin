# Best Practices Testing

## Contents

### `style.py`
`style.py` contains examples of proper styling for a variety of python functions

### `get_column_stats.py`
`get_column_stats.py` contains a function for extracting the mean and standard deviation from a specified column of an input file

### `basics_test.sh`
`basics_test.sh` contains tests to make sure these functions adhere to best practices.

## Usage

To calculate the stats of a column in a file, use `python get_column_stats.py -f <filename> -c <column number>`

To run the tests, use ` . basics_test.sh`

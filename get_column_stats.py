import math
import argparse


def parse_inputs():
    """Parse the arguments for calculating stdev from a column of a text file

    Parameters
    ----------
    None

    Returns
    -------
    filename : str
        Name of the file to be read
    column : int
        Column number of the file to compute stdev for
    """

    parser = argparse.ArgumentParser(
        description='Process input parameters for RJMC 2CLJQ')

    parser.add_argument('--filename', '-f',
                        type=str,
                        help='Name of the file to include',
                        required=True)

    parser.add_argument('--column', '-c',
                        type=int,
                        help='Column number to get stdev for',
                        required=True)
    args = parser.parse_args()

    filename = args.filename
    column = args.column
    return filename, column


def calculate_mean(number_list):
    """Calculate the mean of a column in a file

    Parameters
    ----------

    number_list : list
	list of the numbers to compute the mean of

    Returns
    -------
    mean : float
	mean of the column chosen
    """

    
    mean = sum(number_list)/len(number_list)

    return mean

def calculate_stdev(number_list):
    """Calculate the stdev of a column in a file

    Parameters
    ----------
    number_list : list
	list of the number to compute stdev for
    Returns
    -------
    stdev : float
        Stdev of the column supplied
    """

    mean = sum(number_list)/len(number_list)

    stdev = math.sqrt(sum([(mean-x)**2 for x in number_list]) / len(number_list))

    return stdev


def main():
    filename, column = parse_inputs()

    mean, stdev = calculate_stdev(filename, column)

    print('mean:', mean)
    print('stdev:', stdev)


if __name__ == '__main__':
    main()

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run check_style_style pycodestyle style.py
assert_no_stdout
assert_exit_code 0

run check_style_get_column_stats pycodestyle get_column_stats.py
assert_no_stdout
assert_exit_code 0


(for i in `seq 1 100`; do 
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt



run check_argparse_inputs_failure python get_column_stats.py data.txt $a
assert_stderr
assert_exit_code 2

a=$(( RANDOM % 5))
run check_argparse_inputs_success python get_column_stats.py -f data.txt -c $a
assert_no_stderr
assert_in_stdout stdev
assert_exit_code 0

run check_bad_data_file python get_column_stats.py -f fake.txt -c $a
assert_exit_code 1


V=1
(for i in `seq 1 100`; do 
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data.txt

run check_basic_output_stdev python get_column_stats.py -f data.txt -c $a
assert_in_stdout 'mean: 1'
assert_in_stdout 'stdev: 0'
assert_exit_code 0

#teardown
rm ssshtest
rm data.txt

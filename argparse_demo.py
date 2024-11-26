#!/usr/bin/env python3
import argparse

# Instantiate the parser
parser = argparse.ArgumentParser(description='Optional app description')

# Required positional argument
parser.add_argument('int_arg', type=int,
                    help='First Integer positional argument')

# Optional positional argument
parser.add_argument('opt_int_arg', type=int, nargs='?',
                    help='Optional Second integer positional argument')

# Optional argument
parser.add_argument('--option', type=str,
                    help='An optional string argument')

# Switch
parser.add_argument('--switch', action='store_true',
                    help='A boolean switch')
# Parse
args = parser.parse_args()

# Access

print("Argument values:")
print(args.int_arg)
print(args.opt_int_arg)
print(args.option)
print(args.switch)

# Check Values

if args.opt_int_arg > 10:
    parser.error("Optional 2nd Argument cannot be larger than 10")

if switch:
    print('True')

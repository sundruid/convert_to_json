#!/usr/bin/env python3

import csv
import json
import argparse

def convert_to_json(filename):
    with open(filename, 'r') as f:
        # Trying to detect the file's delimiter
        dialect = csv.Sniffer().sniff(f.read(1024))
        f.seek(0)
        
        reader = csv.reader(f, dialect)

        # Try to use the first line as field names
        fieldnames = next(reader)

        # If field names are not clear, ask the user
        for i, name in enumerate(fieldnames):
            if name.strip() == '':
                fieldnames[i] = input(f"Field {i+1} doesn't have a name. Please enter a name: ")

        # Create a dictionary with fieldnames
        data = [dict(zip(fieldnames, row)) for row in reader]

    return data

def write_to_newline_delimited_json(filename, data):
    with open(filename, 'w') as f:
        for item in data:
            f.write(json.dumps(item))
            f.write('\n')

def parse_arguments():
    parser = argparse.ArgumentParser(description='Convert a text file into a newline-delimited JSON file.')
    parser.add_argument('input_file', help='The input text file to be converted.')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    data = convert_to_json(args.input_file)
    output_file = args.input_file + ".json"
    write_to_newline_delimited_json(output_file, data)

import argparse
import pandas as pd
import json
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import os
# import sys
import threading

def read_data(input_file, input_format):
    try:
        if not os.path.isfile(input_file):
            raise FileNotFoundError(f"Input file not found: {input_file}")

        if input_format not in ['csv', 'json', 'xml']:
            raise ValueError(f"Unsupported input format: {input_format}")

        if input_format == 'json':
            with open(input_file, 'r') as json_file:
                return pd.read_json(json_file)
        elif input_format == 'xml':
            tree = ET.parse(input_file)
            root = tree.getroot()

            data = []
            for child in root:
                record = {}
                for element in child:
                    record[element.tag] = element.text
                data.append(record)

            return pd.DataFrame(data)
        elif input_format == 'csv':
            # Check if the CSV file is empty
            with open(input_file, 'r') as csv_file:
                peek = csv_file.read(1)
                if not peek:
                    return pd.DataFrame()  # Return an empty DataFrame for empty CSV files
                else:
                    # Read the CSV file only if it's not empty
                    return pd.read_csv(input_file, nrows=1)
        else:
            raise ValueError(f"Unsupported input format: {input_format}")
    except FileNotFoundError as e:
        print(f"Error reading input file: {e}")
        raise  # Re-raise the exception for better traceback
    except ValueError as e:
        print(f"Error reading input file: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error reading input file: {e}")
        raise

def write_data(output_file, output_format, data_frame):
    try:
        output_dir = os.path.dirname(output_file)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        if output_format == 'csv':
            data_frame.to_csv(output_file, index=False)
        elif output_format == 'json':
            data_frame.to_json(output_file, orient='records', indent=4)
        elif output_format == 'xml':
            xml_data = data_frame.to_xml(index=False, root_name='data', row_name='record')
            with open(output_file, 'w') as xml_file:
                xml_file.write(xml_data)
        else:
            raise ValueError(f"Unsupported output format: {output_format}")
    except Exception as e:
        print(f"Unexpected error writing output file: {e}")
        raise

def convert_data(input_file, input_format, output_file, output_format):
    input_data = read_data(input_file, input_format)

    if input_data is not None:
        lock = threading.Lock()  # Add this line for thread safety
        with lock:
            write_data(output_file, output_format, input_data)
            print(f'Conversion completed: {input_file} ({input_format}) -> {output_file} ({output_format})')

def main():
    parser = argparse.ArgumentParser(description='Convert data between different formats.')
    parser.add_argument('input_file', help='Input file path')
    parser.add_argument('input_format', help='Input file format (csv, json, xml)')
    parser.add_argument('output_file', help='Output file path')
    parser.add_argument('output_format', help='Output file format (csv, json, xml)')
    parser.add_argument('--concurrency', type=int, default=1, help='Number of concurrent processes or threads')
    parser.add_argument('--concurrency-type', choices=['thread', 'process'], default='thread', help='Concurrency type (thread or process)')

    args = parser.parse_args()

    if args.concurrency > 1:
        executor_type = ThreadPoolExecutor if args.concurrency_type == 'thread' else ProcessPoolExecutor
        with executor_type(max_workers=args.concurrency) as executor:
            futures = [executor.submit(convert_data, args.input_file, args.input_format, args.output_file, args.output_format) for _ in range(args.concurrency)]
    else:
        convert_data(args.input_file, args.input_format, args.output_file, args.output_format)

if __name__ == "__main__":
    main()

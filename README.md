# Data Converter Tool
Simple data converter script written in python by ChatGPT 3.5 for a student prompt enginerring project.

## Prompts Used
"Build a simple cli tool in python that supports all commonly used data formats, concurrency, and error handling. Include unit testing that covers as may edge cases as possible and employs boundary testing while covering all features of the script."

"How can I make this tool more robust?"

"Without knowing what requirements and nature of data the user may have how can I make this tool as complete and universal as possible?"

"
Error I am getting:
Converter Code:
Test Code:
"

## Readme Format Generated by ChatGPT and Tailored by Lauren

### Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Usage](#usage)
- [Options](#options)
- [Examples](#examples)
- [License](#license)

### Overview

The Data Conversion Tool simplifies the process of converting data files from one format to another, supporting CSV, JSON, and XML. Whether you need to convert large datasets or individual files, this tool provides a seamless solution.

### Features

- **Format Support:** Convert data between CSV, JSON, and XML formats.
- **Concurrency:** Utilize multiple processes or threads for faster conversions.
- **Error Handling:** Robust error handling for file-related issues and unsupported formats.
- **Versatility:** Easily integrate the tool into your workflow for diverse data conversion needs.

### Usage
The tool uses a command-line interface. Here are some basic examples:

`pip install -r requirements.txt`

For additional options and details, run:

`python data_converter.py --help`

### Options
The tool supports the following command-line options:

* **input_file**: Path to the input file.
* **input_format**: Format of the input file (csv, json, xml).
* **output_file**: Path to the output file.
* **output_format**: Format of the output file (csv, json, xml).
* **--concurrency**: Number of concurrent processes or threads.
* **--concurrency-type**: Concurrency type (thread or process).

### Examples
Convert CSV to JSON:

`python data_converter.py input.csv csv output.json json`

Convert XML to CSV with concurrency:

`python data_converter.py input.xml xml output.csv csv --concurrency 4 --concurrency-type process`

### License
This project is licensed under the MIT License.
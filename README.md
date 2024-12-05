# json2jsonl

**json2jsonl** is a simple Python utility for converting JSON files (containing arrays of objects) into JSON Lines (JSONL) format. 
JSONL is a lightweight and efficient data serialization format where each line represents a single JSON object.

## Features

- Converts JSON files with arrays into JSONL format.
- Handles large JSON files efficiently by processing objects line by line.
- Easy to use with minimal setup.

## Installation

To use this tool, you need Python 3.11 or later and the `jsonlines` library. Install the required dependencies with:

```bash
pip install jsonlines

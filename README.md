# File Type Identifier

A Python tool to identify file types by their magic numbers (file signatures) and detect file type spoofing.

## Features

- Identifies file types by reading file headers (magic numbers)
- Detects file type spoofing (when a file's extension doesn't match its actual type)
- Supports 100+ file types including documents, images, archives, executables, and more
- Works offline using a local signatures database
- Easy to extend with new file signatures

## Project Structure

```
file_type_identifier/
├── src/
│   └── file_identifier/
│       ├── __init__.py      # Package initialization and exports
│       ├── database.py      # Loads signatures from JSON database
│       ├── checker.py       # Checks individual files against signatures
│       └── scanner.py       # Scans directories and processes files
├── data/
│   └── signatures.json      # File signatures database (extension -> hex signature)
├── uploads/                 # Default directory for files to scan
├── main.py                  # Main entry point with CLI argument parsing
├── requirements.txt         # Dependencies (none - uses standard library only)
└── README.md               # This file
```

## How It Works

### Database Module (`database.py`)
- `get_project_root()`: Calculates the project root directory by going up two levels from the module location (file_identifier -> src -> project_root)
- `load_signatures()`: Loads the signatures database from `data/signatures.json`. Returns a dictionary mapping file extensions to their hexadecimal magic number signatures. Handles file not found and JSON parsing errors gracefully.

### Checker Module (`checker.py`)
- `check_file(file_path, signatures)`: 
  - Extracts the claimed file extension from the filename
  - Reads the first 8 bytes of the file in binary mode and converts them to hexadecimal
  - Compares the hex header against all known signatures in the database
  - Returns a tuple: (status, detected_type, claimed_extension, header)
    - status: 'valid' (extension matches), 'spoofed' (extension doesn't match), 'unknown' (no match found), or 'error' (read failed)
    - detected_type: The file type found in database or None
    - claimed_extension: The extension from filename or None
    - header: The hex representation of file header or None
- `format_result()`: Formats the check results into human-readable output strings for display

### Scanner Module (`scanner.py`)
- `scan_directory(directory_path)`:
  - Validates that the directory exists and is actually a directory
  - Loads the signatures database
  - Iterates through all files in the directory
  - For each file, calls `check_file()` and formats the result
  - Prints formatted results showing VALID, SPOOFED, UNKNOWN, or ERROR status

### Main Entry Point (`main.py`)
- Uses argparse to handle command-line arguments
- `get_default_uploads_dir()`: Calculates the default uploads directory path relative to project root
- `main()`: Parses command-line arguments, determines which directory to scan (custom or default), and calls `scan_directory()`

### Package Initialization (`__init__.py`)
- Defines package version
- Exports main functions: `load_signatures`, `check_file`, `scan_directory`
- Makes the package importable and provides clean API

## Installation

1. Clone or download this repository
2. No external dependencies required - uses only Python standard library (os, json, argparse)

## Usage

### Basic Usage

Scan the default `uploads/` directory:
```bash
python main.py
```

### Custom Directory

Scan a specific directory:
```bash
python main.py -d /path/to/directory
python main.py --directory ./my_files
```

### Command Line Options

```
python main.py [-h] [-d DIRECTORY]

Options:
  -h, --help            Show help message
  -d, --directory DIR   Directory to scan (default: ./uploads)
```

## Output

The tool will output one of the following for each file:

- **VALID**: File extension matches the detected file type
- **SPOOFED**: File extension doesn't match the detected file type (potential security risk)
- **UNKNOWN**: File type could not be identified (header doesn't match any known signature)
- **ERROR**: An error occurred while reading the file (permissions, corruption, etc.)

Example output:
```
Scanning directory: ./uploads
Loaded 167 file type signatures.

 VALID: ./uploads/document.pdf (PDF)
 SPOOFED: ./uploads/malware.exe claims .txt but is EXE
 UNKNOWN: ./uploads/unknown.bin (Header: 1a2b3c4d5e6f7a8b)
```

## Adding New File Signatures

Edit `data/signatures.json` to add new file type signatures. The format is a JSON object where keys are file extensions and values are hexadecimal magic numbers:

```json
{
  "pdf": "25504446",
  "zip": "504b0304",
  "png": "89504e47"
}
```

The signature should be the hexadecimal representation of the file's magic number (usually the first few bytes). You can find magic numbers by:
1. Opening a file in a hex editor
2. Reading the first few bytes
3. Converting them to hexadecimal
4. Adding the extension and hex signature to the JSON file

## Technical Details

- **File Reading**: Files are opened in binary mode (`'rb'`) to read raw bytes without encoding issues
- **Header Size**: Currently reads first 8 bytes, which is sufficient for most file types
- **Case Sensitivity**: Signatures are compared case-insensitively (converted to lowercase)
- **Path Handling**: All paths are resolved relative to project root using `os.path` functions
- **Error Handling**: Graceful error handling for missing files, invalid JSON, and file read errors

## License

This project is open source and available for use.

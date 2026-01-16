#!/usr/bin/env python3

import os
import argparse
from src.file_identifier.scanner import scan_directory


def get_default_uploads_dir():
    project_root = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(project_root, 'uploads')


def main():
    parser = argparse.ArgumentParser(description='File Type Identifier - Detect file types by magic numbers')
    
    parser.add_argument(
        '-d', '--directory',
        type=str,
        default=None,
        help='Directory to scan (default: ./uploads)'
    )
    
    args = parser.parse_args()
    
    if args.directory:
        directory = args.directory
    else:
        directory = get_default_uploads_dir()
    
    scan_directory(directory)


if __name__ == "__main__":
    main()

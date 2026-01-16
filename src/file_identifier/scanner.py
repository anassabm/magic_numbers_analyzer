import os
from .database import load_signatures
from .checker import check_file, format_result


def scan_directory(directory_path):
    if not os.path.exists(directory_path):
        print(f"Error: Directory '{directory_path}' does not exist.")
        return
    
    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a directory.")
        return
    
    signatures = load_signatures()
    
    if not signatures:
        print("Warning: No signatures loaded. Cannot identify file types.")
        return
    
    print(f"Scanning directory: {directory_path}")
    print(f"Loaded {len(signatures)} file type signatures.\n")
    
    files_found = 0
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        if os.path.isfile(file_path):
            files_found += 1
            status, detected_type, claimed_ext, header = check_file(file_path, signatures)
            result = format_result(file_path, status, detected_type, claimed_ext, header)
            print(result)
    
    if files_found == 0:
        print("No files found in the directory.")

import os

# 1. Our "Database" of signatures
SIGNATURES = {
    "jpg": "ffd8ff",
    "png": "89504e47",
    "pdf": "25504446",
    "zip": "504b0304"
}

def check_file(file_path):
    # Get the extension from the filename (e.g., "jpg")
    ext = file_path.split('.')[-1].lower()
    
    if ext not in SIGNATURES:
        print(f"Skipping: {ext} is not in our database.")
        return

    # 2. Open file in Read Binary ('rb') mode
    with open(file_path, 'rb') as f:
        # Read the first 4 bytes
        header = f.read(4)
        
        # 3. Convert bytes to a hex string
        file_hex = header.hex()
        
    # 4. Compare
    expected_hex = SIGNATURES[ext]
    
    if file_hex.startswith(expected_hex):
        print(f"[✅] VALID: {file_path} matches its identity.")
    else:
        print(f"[⚠️] ALERT: {file_path} mismatch!")
        print(f"    Expected: {expected_hex}, Found: {file_hex}")

# Example usage:
# check_file("test_image.jpg")
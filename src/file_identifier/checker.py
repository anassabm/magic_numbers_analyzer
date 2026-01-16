def check_file(file_path, signatures):
    try:
        claimed_ext = file_path.split('.')[-1].lower() if '.' in file_path else None
        
        with open(file_path, 'rb') as f:
            header = f.read(8).hex()
        
        detected_type = None
        for known_ext, sig in signatures.items():
            if header.startswith(sig.lower()):
                detected_type = known_ext
                break
        
        if detected_type:
            if claimed_ext and claimed_ext == detected_type.lower():
                return 'valid', detected_type, claimed_ext, header
            else:
                return 'spoofed', detected_type, claimed_ext, header
        else:
            return 'unknown', None, claimed_ext, header
            
    except Exception:
        return 'error', None, None, None


def format_result(file_path, status, detected_type, claimed_ext, header=None):
    if status == 'valid':
        return f" VALID: {file_path} ({detected_type.upper()})"
    elif status == 'spoofed':
        return f" SPOOFED: {file_path} claims .{claimed_ext} but is {detected_type.upper()}"
    elif status == 'unknown':
        header_display = header[:16] if header else 'N/A'
        return f" UNKNOWN: {file_path} (Header: {header_display})"
    else:
        return f" ERROR reading {file_path}"

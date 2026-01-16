import os
import json


def get_project_root():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(os.path.dirname(current_dir))


def load_signatures():
    project_root = get_project_root()
    signatures_path = os.path.join(project_root, 'data', 'signatures.json')
    
    if os.path.exists(signatures_path):
        try:
            with open(signatures_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading signatures database: {e}")
            return {}
    else:
        print(f"Warning: Signatures database not found at {signatures_path}")
        return {}

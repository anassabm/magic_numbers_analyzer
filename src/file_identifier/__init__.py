__version__ = "1.0.0"

from .database import load_signatures
from .checker import check_file
from .scanner import scan_directory

__all__ = ['load_signatures', 'check_file', 'scan_directory']

import os
import sys

EXCLUDE_EXTENSIONS = {
    '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico', '.pdf',
    '.bmp', '.zip', '.tar', '.gz', '.rar', '.7z', '.woff', '.woff2'
}

REPLACEMENTS = {
    'ERPNext': 'Syncera',
    'Frappe Technologies Pvt. Ltd.': 'Aixton'
}

def is_binary_file(path):
    try:
        with open(path, 'rb') as f:
            chunk = f.read(1024)
            if b'\0' in chunk:
                return True
    except Exception:
        return True
    return False

def process_file(path):
    if is_binary_file(path):
        return False
    ext = os.path.splitext(path)[1].lower()
    if ext in EXCLUDE_EXTENSIONS:
        return False
    try:
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
    except UnicodeDecodeError:
        return False
    original = text
    for old, new in REPLACEMENTS.items():
        text = text.replace(old, new)
    if text != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
        return True
    return False

def main(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for name in filenames:
            file_path = os.path.join(dirpath, name)
            if process_file(file_path):
                print(f'Modified: {file_path}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python scripts/rebrand.py <path>')
        sys.exit(1)
    main(sys.argv[1])


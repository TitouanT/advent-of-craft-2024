import hashlib
import os
from base64 import b64encode

from typing import Protocol

class HashAlgo(Protocol):
    def update(data: bytes) -> None: ...
    def digest() -> bytes: ...

def convert(data: str, strategie: HashAlgo) -> str:
    strategie.update(data.encode('utf8'))
    return b64encode(strategie.digest()).decode('utf8')

def convert_key(key: str) -> str:
    return convert(key, hashlib.sha256())

def convert_iv(iv: str) -> str:
    return convert(iv, hashlib.md5())

def load_file(filename):
    path = os.path.join(os.path.dirname(__file__), 'resources', filename)
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

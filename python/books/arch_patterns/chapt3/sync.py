"""
Script for synchronizing tow file directories, source and destination
Requirements:
  - If file exists in source and not in destination, copy the file over.
  - If file exists in source but different name in destination, rename.
  - If file exists in destination and not in source, delete.
"""
import hashlib
import os
from pathlib import Path
import shutil

BLOCKSIZE = 65536

def hash_file(path) -> str:
    """Given a file path, return hash of the file"""
    hasher = hashlib.sha1()
    with path.open("rb") as file:
        buf = file.read(BLOCKSIZE)
        while buf:
            hasher.update(buf)
            buf = file.read(BLOCKSIZE)
    return hasher.hexdigest()

def sync(source, destination):
    """Synchronize files in tow directories"""
    # walk the source dir and build a dict of filenames and their hashes
    source_hashes = {}
    for folder, _, files in os.walk(source):
        for filename in files:
            source_hashes[hash_file(Path(folder) / filename)] = filename

    # keep track of files found
    seen = set()

    # walk the destination dir and get filenames and hashes
    for folder, _, files in os.walk(destination):
        for filename in files:
            dest_path = Path(folder) / filename
            dest_hash = hash_file(dest_path)
            seen.add(dest_hash)

            # DELETE, if file in destination and not source
            if dest_hash not in source_hashes:
                dest_path.remove()

            # RENAME, if hash match but filename
            elif dest_hash in source_hashes and filename != source_hashes[dest_hash]:
                shutil.move(dest_path, Path(folder) / source_hashes[dest_hash])

    for src_hash, filename in source_hashes.items():
        if src_hash not in seen:
            shutil.copy(Path(source) / filename, Path(destination) / filename)

if __name__ == '__main__':
    sync(
        "/Users/brianlynch/Desktop/personal/code_scratchpad/python/books/arch_patterns/chapt3/source",
        "/Users/brianlynch/Desktop/personal/code_scratchpad/python/books/arch_patterns/chapt3/destination")
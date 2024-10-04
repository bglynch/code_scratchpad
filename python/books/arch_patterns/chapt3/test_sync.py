
from pathlib import Path
import shutil
import tempfile
from .sync import sync


def test_when_a_file_exists_in_the_source_but_not_the_destination():
    try:
        # create temp dirs
        source = tempfile.mkdtemp()
        destination = tempfile.mkdtemp()

        # create file in source directory
        content = "Test string in file"
        (Path(source) / "my-file").write_text(content)

        sync(source, destination)

        # expect file to exist in destination
        expected_path = Path(destination) / "my-file"
        assert expected_path.exists()
        assert expected_path.read_text() == content
    finally:
        shutil.rmtree(source)
        shutil.rmtree(destination)

def test_when_a_file_has_been_renamed_to_in_the_source():
    try:
        # create temp dirs
        source = tempfile.mkdtemp()
        destination = tempfile.mkdtemp()

        # create file in source directory
        content = "I am a file that was rename"
        source_path = Path(source) / "source-filename"
        old_dest_path = Path(source) / "dest-filename"
        expected_dest_path = Path(source) / "source-filename"

        source_path.write_text(content)
        old_dest_path.write_text(content)

        sync(source, destination)

        assert old_dest_path.exists() is False
        assert expected_dest_path.read_text() == content
    finally:
        shutil.rmtree(source)
        shutil.rmtree(destination)

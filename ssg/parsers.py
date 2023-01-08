from typing import List
from pathlib import Path
import shutil


class Parser:
    extensions = List[str]

    def valid_extension(self, extension):
        if extension in self.extensions:
            return True

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    @staticmethod
    def read(path):
        with open(path) as file:
            return file.read()

    @staticmethod
    def write(path: Path, dest: Path, content, ext='.html'):
        full_path = dest / path.with_suffix(ext).name

        with open(full_path) as file:
            file.write(content)

    @staticmethod
    def copy(path: Path, source: Path, dest: Path):
        shutil.copy2(path, dest / path.relative_to(source))


class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        Parser.copy(path, source, dest)

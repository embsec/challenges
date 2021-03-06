from core import LessonFactory
from pathlib import Path
import shutil


def setup(lesson_path):
    for name in Path(__file__).parent.glob('*'):
        if not name.is_dir():
            shutil.copy(name, Path(lesson_path) / name.name)
        else:
            shutil.copytree(name, Path(lesson_path) / name.name)


lesson = LessonFactory('reverse_engineering', setup=setup)

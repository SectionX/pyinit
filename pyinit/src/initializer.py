#!/usr/bin/python3

from pathlib import Path
import venv
import sys
import os


def initialize_project(template, app_name):

    CWD = Path.cwd()
    TEMPLATE = Path(__file__).parent.parent / 'data' / 'templates' / template
    if not TEMPLATE.exists():
        print(f'Error: Template {template} could not be found.', file=sys.stderr)
        sys.exit(1)

    walk = os.walk(str(TEMPLATE))

    for item in walk:
        path, dirs, files = item
        path += os.sep

        sample_path = Path(path)
        sample_files = [sample_path / item for item in files]

        target_path = (CWD / path.rsplit(template+'/')[-1].replace('app_name', app_name))
        target_dirs = [target_path / item.replace('app_name', app_name) for item in dirs]
        target_files = [target_path / item.removesuffix('.sample') for item in files]

        for target in target_dirs:
            print(f'Creating directory {str(target)}')
            target.mkdir()

        for sample, target in zip(sample_files, target_files):
            print(f'Creating file {str(target)}')
            text = sample.read_text().replace('{app_name}', app_name)
            target.write_text(text)

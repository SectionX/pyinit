#!/usr/bin/python3

from pathlib import Path
import venv
import sys

def main():

    CWD = Path('.').absolute()

    try:
        app_name = sys.argv[1]
    except Exception:
        app_name = CWD.name
        user_input = input(f'No app name was given, do you want it to be {app_name} (Y/n)?')
        if user_input == '' or user_input.lower() == 'y':
            pass
        else:
            print('Stopping execution.')
            sys.exit(1)

    APP_PATH = CWD / app_name
    SRC_PATH = APP_PATH / 'src'
    TEST_PATH = APP_PATH / 'tests'
    DOCS_PATH = APP_PATH / 'docs'
    DATA_PATH = APP_PATH / 'data'

    APP_PATH.mkdir()
    SRC_PATH.mkdir()
    TEST_PATH.mkdir()
    DOCS_PATH.mkdir()
    DATA_PATH.mkdir()

    with (CWD / 'setup.py').open('w') as setup:
        setup.write(
    '''
from setuptools import setup

setup()
    '''
    )

    with (CWD / 'pyproject.toml').open('w') as toml:
        toml.write(
    f'''
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "{app_name}"
version = "0.1"
dependencies = []
requires-python = ">=3.8"
authors = [
{{name = "MyName", email = "MyName@email.com"}},
]
maintainers = []
description = "Initialize a basic project structure for your new python app"
readme = "README.md"
license = {{file = "LICENSE"}}
keywords = ["add", "keywords", "for", "pypa"]
classifiers = [
"Programming Language :: Python",
]

[tool.setuptools]
packages = ['{app_name}', '{app_name}.src']

[project.optional-dependencies]

[project.urls]
Homepage = ""
Documentation = ""
Repository = ""
"Bug Tracker" = ""
Changelog = ""

[project.scripts]
{app_name} = "{app_name}:__main__.main()"

[project.gui-scripts]

[project.entry-points]
'''
)

    with (CWD / 'install.sh').open('w') as install:
        install.write(
'''#!/usr/bin/bash

source venv/bin/activate
python3 -m pip install .
'''
    )
        
    with (CWD / 'uninstall.sh').open('w') as uninstall:
        uninstall.write(
    f'''#!/usr/bin/bash

python3 -m pip uninstall -y {app_name}
deactivate
    '''
    )
        
    with (CWD / '.gitignore').open('w') as gitignore:
        gitignore.write(
    '''install.sh
uninstall.sh
build/
pyinit.egg-info
**/__pycache__
    '''
    )

    with (CWD / 'LICENSE').open('w') as license:
        license.write(
    '''Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.'''
    )

    (CWD / 'requirements.txt').open('w').close()
    (CWD / 'README.md').open('w').close()
    (APP_PATH / '__init__.py').open('w').close()
    (APP_PATH / '__main__.py').open('w').close()
    (SRC_PATH / '__init__.py').open('w').close()
    (TEST_PATH / '__init__.py').open('w').close()

    venv.main(['venv'])


if __name__ == '__main__':
    main()
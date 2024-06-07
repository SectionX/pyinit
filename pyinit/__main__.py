import sys
import pathlib
import argparse
import venv
from pyinit.src.initializer import initialize_project

parser = argparse.ArgumentParser(__name__.split('.')[0], description='Initialize Python Projects')
parser.add_argument('-t', '--type', required=False, default='basic-cli', help='Choose between available project types. Type "pyinit list" to see the available templates')
parser.add_argument('-n', '--name', required=False, default='', action='store')
parser.add_argument('--no-venv', required=False, default=False, action='store_true', help='Add this option if you don\'t want to use Python\'s venv module')
parser.add_argument('--list', default=False, action='store_true', help='Shows a list of available project templates and exits')

def main():

    args = parser.parse_args()
    _type = args.type
    _name = args.name
    _list_only = args.list
    _no_venv = args.no_venv

    if _list_only:
        template_path = pathlib.Path(__file__).parent / 'data' / 'templates'
        print(*[item.name for item in template_path.iterdir()],end='\n')
        sys.exit(0)

    if _name:
        if '-' in _name:
            print('Implicitly replacing - with _ because it creates conflicts.')
            print('If you want to use the original name in scripts, edit the [project.scripts] section of pyproject.toml') 
        app_name = _name.replace('-', '=')
    else:
        app_name = pathlib.Path.cwd().name.replace('-', '_')
        user_input = input(f'No app name was given, do you want it to be {app_name} (Y/n)?')
        if not (user_input == '' or user_input.lower() == 'y'):
            print('Stopping execution.')
            sys.exit(1)

    initialize_project(_type, app_name)
    if _no_venv:
        sys.exit()
    else:
        venv.main(['venv'])
    print(args)

if __name__ == '__main__':
    main()

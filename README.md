A simple script to initialize python projects.

# Installation:
Download the repo
Make sure you are in the directory containing the setup.py file.
pip install .

I haven't made this available to pypi so you will have to
do it manually.

# To initialize a project:
Make a directory for your new project and cd into it.
pyinit YourProjectName

pyinit will create a basic structure

app/src/
app/tests/
app/__main__.py

some basic package conf files
an MIT License

along with two scripts
install.sh
uninstall.sh

The install.sh script activates the venv before
doing anything, so you won't install globally
accidentally.

By default the toml file is configured to create
a command with your appname in the terminal.

This script will run the main() function of __main__.py file.

# Why did I make this:
For practice mostly and because testing doesn't work well
if you setup your directory incorrectly due to import issues.
So it's tiresome to write all these files every time you want
to make a simple app/script.

By creating a project structure like this and installing it
to the virtual environment, python understands that this
is a package, so it deals with import issues.

Packaging isn't simple and Python packaging is even more complex
because of the language's versatility. The easily accessible 
information doesn't explain well how it works. This little app 
may help you get started quicker by providing an example that 
you can expand upon. 

Because no matter how much you read about it, there is no 
such thing as "it almost works" in programming.
It will either run or spam your terminal with red messages.

# Some beginner advice:
If you found your way to this repo, you probably have some
trouble making relative imports work, or you broke your teeth
because you can't make your test scripts run, or you messed up
pathing and your app only works when run in your computer under
very specific circumstances.

Getting intimately familiar with the current working directory
is important. While it would take too long to explain how this
works, one simple piece of advice that I wish someone told me
earlier, is that you should try to run your code from outside
the project directory, otherwise you will make mistakes with
either pathing or imports.

Forget about relative pathing and get used to __file__ dunder
and the pathing module. Always use paths relative to either
the package top directory, or the module you are importing.

Being capable of running your code outside of the code directory
is the first step to creating distributable applications.




from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if not line.startswith('#') and line.strip() != '']

setup(
    name='frida-ios-dump',
    py_modules=['dump'],
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['dump.js']},
    entry_points={
        'console_scripts': [
            'frida-ios-dump=dump.dump:main',
        ],
    },
)
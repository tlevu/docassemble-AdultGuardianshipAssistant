import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.AdultGuardianshipAssistant',
      version='0.0.1',
      description=('A package that helps individuals petition the court to assign a guardian to an incapacitated adult.'),
      long_description='<<<<<<< HEAD\r\n# docassemble.AdultGuardianshipAssistant\r\n\r\nA package that helps individuals petition the court to assign a guardian to an incapacitated adult.\r\n\r\n## Author\r\n\r\nkwilson5@su.suffolk.edu\r\n\r\n=======\r\n# docassembe-AdultGuardianshipAssistant\r\nA guided interview to help petitioners collect and compile the appropriate court forms.\r\n\r\n## Author\r\n\r\nKisha Wilson\r\nkwilson5@su.suffolk.edu\r\n\r\nThomas Levu\r\ntlevu@su.suffolk.edu\r\n\r\n## Disclaimer\r\n\r\nThis form has been created for a class project and should not be considered legal advice or services.\r\n>>>>>>> main\r\n',
      long_description_content_type='text/markdown',
      author='Kisha Wilson & Mallory Ursul',
      author_email='kwilson5@su.suffolk.edu',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/AdultGuardianshipAssistant/', package='docassemble.AdultGuardianshipAssistant'),
     )


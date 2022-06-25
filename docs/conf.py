import os
import sys

sys.path.insert(0, os.path.abspath('..'))

import utilitools

project = 'utilitools'
author = 'Idan Hazan'
copyright = f'2022, {author}'
version = utilitools.__version__
html_theme = 'sphinx_rtd_theme'
extensions = [
    'readthedocs_ext.readthedocs',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx_toolbox.more_autodoc',
    'sphinx.ext.autodoc',
]

import os
import sys

sys.path.insert(0, os.path.abspath('..'))

import utilitools

project = 'utilitools'
author = 'Idan Hazan'
copyright = f'2022, {author}'
html_theme = 'sphinx_rtd_theme'
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

import datetime
import os
import pathlib
import sys
sys.path.insert(0, os.path.abspath(os.path.join("..")))  # adds path to find greykite folder during doc build.

from sphinx_gallery.sorting import FileNameSortKey

from greykite.common.sphinx_plotly import plotly_sg_scraper

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = u'Greykite Library'
copyright = u'{year}, LinkedIn'.format(year=datetime.datetime.today().year)
author = u''


# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',  # this order is important to make intersphinx work!
    'sphinx.ext.autosummary',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx_gallery.gen_gallery',
]

autodoc_default_options = {
    'members': None,
    'inherited-members': None,
    'member-order': 'bysource',
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['templates']

# generate autosummary even if no references
autosummary_generate = True

# The reST default role (used for this markup: `text`) to use for all documents.
default_role = "autolink"

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'templates', 'Thumbs.db', '.DS_Store']

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'greykite_doc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Greykite.tex', 'Greykite Documentation',
     'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'greykite', 'Greykite Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Greykite', 'Greykite Documentation',
     author, 'Greykite', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

# Registers the plotly scraper
# Adapted from: https://github.com/plotly/plotly-sphinx-gallery/blob/master/docs/conf.py
image_scrapers = ('matplotlib', plotly_sg_scraper,)  # supports matplotlib and plotly images

parent_path = pathlib.Path(__file__).parent.absolute()
default_thumb_file = os.path.join(parent_path, 'nbpages', 'default_thumb.png')

sphinx_gallery_conf = {
    # path to python examples
    'examples_dirs': [
        'nbpages/quickstart',
        'nbpages/tutorials',
        'nbpages/templates'
    ],
    # where to save gallery generated output (added to gitignore)
    'gallery_dirs': [
        'gallery/quickstart',
        'gallery/tutorials',
        'gallery/templates'
    ],
    'within_subsection_order': FileNameSortKey,  # alphanumeric order within a gallery
    'line_numbers': True,
    'download_all_examples': False,  # control at file level
    'filename_pattern': '/.*',  # executed files
    'ignore_pattern': r'__init__\.py',  # not executed or added to gallery
    'min_reported_time': 10,  # does not show runtime if below this threshold (seconds)
    'reference_url': {
        # the module you locally document uses None
        # the rest are identified by intersphinx
        'sphinx_gallery': None,
    },
    'image_scrapers': image_scrapers,
    # 'default_thumb_file': default_thumb_file,
    'capture_repr': ('_repr_html_', '__repr__'),
}

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True  # we prefer this one
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

# -- Options for intersphinx extension ---------------------------------------

intersphinx_mapping = {
    'numpy': ('https://numpy.org/devdocs/', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/version/0.24.2/', None),
    'plotly': ('https://plotly.com/python-api-reference/', None),
    'python': ('http://docs.python.org/3.7/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None),
    'sklearn': ('https://scikit-learn.org/0.24/', None),
    'stasmodels': ('https://www.statsmodels.org/v0.10.1/', None)
}

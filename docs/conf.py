#!/usr/bin/env python

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

import confluent_cloud_sdk

extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode"]
templates_path = ["_templates"]

# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "Confluent Admin API SDK"
copyright = "2022, John Preston"
author = "John Preston"

version = confluent_cloud_sdk.__version__
# The full version, including alpha/beta/rc tags.
release = confluent_cloud_sdk.__version__
language = None
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output -------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

import sphinx_material

extensions += [
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.autodoc",
]

sitemap_locales = ["en"]
autosummary_generate = True
autoclass_content = "class"

html_baseurl = "https://docs.confluent-cloud-sdk.compose-x.io"

extensions.append("sphinx_material")
html_theme_path = sphinx_material.html_theme_path()
html_context = sphinx_material.get_html_context()
html_theme = "sphinx_material"
# Theme options are theme-specific and customize the look and feel of a
# theme further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    # Set the name of the project to appear in the navigation.
    "nav_title": "Confluent Cloud SDK",
    # Set you GA account ID to enable tracking
    # 'google_analytics_account': 'UA-XXXXX',
    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    "base_url": "https://docs.confluent-cloud-sdk.compose-x.io",
    "html_minify": False,
    "html_prettify": True,
    "css_minify": True,
    # Set the color and the accent color
    "color_primary": "blue",
    "color_accent": "light-blue",
    # Set the repo location to get a badge with stats
    "repo_url": "https://github.com/compose-x/confluent-cloud-sdk/",
    "repo_name": "compose-x/confluent-cloud-sdk",
    "repo_type": "github",
    # Visible levels of the global TOC; -1 means unlimited
    "globaltoc_depth": 2,
    # If False, expand all TOC entries
    "globaltoc_collapse": True,
    # If True, show hidden TOC entries
    "globaltoc_includehidden": False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_show_sourcelink = True
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

# -- Options for HTMLHelp output ---------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "confluent_cloud_sdkdoc"


# -- Options for LaTeX output ------------------------------------------

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
# (source start file, target name, title, author, documentclass
# [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "confluent_cloud_sdk.tex",
        "Confluent Admin API SDK Documentation",
        "John Preston",
        "manual",
    ),
]

# -- Options for manual page output ------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (
        master_doc,
        "confluent_cloud_sdk",
        "Confluent Admin API SDK Documentation",
        [author],
        1,
    )
]

# -- Options for Texinfo output ----------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "confluent_cloud_sdk",
        "Confluent Admin API SDK Documentation",
        author,
        "confluent_cloud_sdk",
        "One line description of project.",
        "Miscellaneous",
    ),
]

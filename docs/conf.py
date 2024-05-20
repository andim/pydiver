# Configuration file for the Sphinx documentation builder.

# -- Project information

project = "Pydiver"
copyright = "2023-2024, Q-Immuno Lab (Andreas Tiffeau-Mayer and team)"
author = "Q-Immuno Lab"

import sys
import os

sys.path.insert(0, os.path.abspath("../"))
import pydiver

version = pydiver.__version__
release = pydiver.__version__


# -- General configuration

extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.linkcode",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for HTML output

html_theme = "sphinx_rtd_theme"

# -- Options for EPUB output
epub_show_urls = "footnote"

# Resolve function for the linkcode extension.
# Modified from
# https://github.com/numpy/numpy/blob/master/doc/source/conf.py#L425

import inspect

lineno = True


def linkcode_resolve(domain, info):
    """
    Determine the URL corresponding to Python object
    """
    if domain != "py":
        return None

    modname = info["module"]
    fullname = info["fullname"]

    submod = sys.modules.get(modname)
    if submod is None:
        return None

    obj = submod
    for part in fullname.split("."):
        try:
            obj = getattr(obj, part)
        except Exception:
            return None

    try:
        fn = inspect.getsourcefile(obj)
    except Exception:
        fn = None
    if not fn:
        return None

    try:
        source, lineno = inspect.getsourcelines(obj)
    except Exception:
        lineno = None

    fn = os.path.relpath(fn, start=os.path.dirname(pydiver.__file__))

    if lineno:
        linespec = "#L%d-L%d" % (lineno, lineno + len(source) - 1)
    else:
        linespec = ""

    return "https://github.com/andim/pydiver/blob/v%s/pydiver/%s%s" % (
        pydiver.__version__,
        fn,
        linespec,
    )

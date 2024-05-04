# opt
opt source code.

## 0. sphinx の使い方

### sphinx install
<pre>
$ pip install sphinx
</pre>

### docファイルの生成
<pre>
$ sphinx-quickstart doc
Welcome to the Sphinx 7.3.7 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Selected root path: doc

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]:

The project name will occur in several places in the built documentation.
> Project name: tsp-sample
> Author name(s): s-muramoto
> Project release []: 1.0.1

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
> Project language [en]: ja
</pre>

### conf.pyの設定
<pre>
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
import sphinx_rtd_theme
import sphinx_fontawesome

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'tsp-sample'
copyright = '2024, s-muramoto'
author = 's-muramoto'
release = '1.0.1'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc', 
    'sphinx.ext.napoleon', 
    'sphinx_rtd_theme', 
    'sphinx_fontawesome', 
    'myst_parser', 
]
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
templates_path = ['_templates']
language = 'en'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_show_sourcelink = False
html_static_path = ['_static']
</pre>

### ドキュメント用rst生成
<pre>
sphinx-apidoc --force -o doc/source/resources src
</pre>

#### モジュールrstの編集 (エラーになる場合)
<pre>
.. automodule:: model
↓ 
.. automodule:: src.model  
※ model.rst, post_processing.rst, pre_processing.rst, tsplib_data.rstを修正
</pre>

#### index.rstの編集
<pre>
.. toctree::
   :maxdepth: 2
   :caption: Contents:


   resources/modules.rst ← 追加
</pre>

### ビルド
<pre>
$ make html
Running Sphinx v7.3.7
loading pickled environment... done
myst v3.0.1: MdParserConfig(commonmark_only=False, gfm_only=False, enable_extensions=set(), disable_syntax=[], all_links_external=False, links_external_new_tab=False, url_schemes=('http', 'https', 'mailto', 'ftp'), ref_domains=None, fence_as_directive=set(), number_code_blocks=[], title_to_header=False, heading_anchors=0, heading_slug_func=None, html_meta={}, footnote_transition=True, words_per_minute=200, substitutions={}, linkify_fuzzy_links=True, dmath_allow_labels=True, dmath_allow_space=True, dmath_allow_digits=True, dmath_double_inline=False, update_mathjax=True, mathjax_classes='tex2jax_process|mathjax_process|math|output_area', enable_checkboxes=False, suppress_warnings=[], highlight_code_blocks=True)
building [mo]: targets for 0 po files that are out of date
writing output...
building [html]: targets for 6 source files that are out of date
updating environment: [config changed ('language')] 6 added, 0 changed, 0 removed
reading sources... [100%] source/resources/tsplib_data
C:\Users\s-chu\OneDrive\ドキュメント\work\python\opt\tsplib\doc\index.rst:9: WARNING: toctree contains reference to nonexisting document 'resources/modules'
looking for now-outdated files... none found
pickling environment... done
checking consistency... C:\Users\s-chu\OneDrive\ドキュメント\work\python\opt\tsplib\doc\source/resources/modules.rst: WARNING: document isn't included in any toctree
done
preparing documents... done
copying assets... copying static files... done
copying extra files... done
done
writing output... [100%] source/resources/tsplib_data
generating indices... genindex py-modindex done
writing additional pages... search done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 2 warnings.

The HTML pages are in _build\html.
</pre>

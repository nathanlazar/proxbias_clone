from setuptools import find_packages, setup

import roadie

setup(
    packages=find_packages(),
    version=roadie.infer_version("{{cookiecutter.python_name}}"),
  {%- if cookiecutter.cli == 'y' %}
    entry_points={"console_scripts": ["{{cookiecutter.python_name}}={{cookiecutter.python_name}}.cli:cli"]},
  {%- endif %}
)

from setuptools import setup

setup(
    name="{{cookiecutter.project_slug}}",
    version="1.0",
    py_modules=["{{cookiecutter.project_slug}}"],
    include_package_data=True,
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        {{cookiecutter.project_slug}}=app:main
    """,
)
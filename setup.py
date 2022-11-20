from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup (
    name='ausData',
    version='0.0.1',
    description= 'Generate and validate Australian related data such as ABN, ACN, TFN.',
    py_modules=["ausData"],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: Freely Distributable"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
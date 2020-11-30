"""lambdata - a collection of Data Science functions"""
import setuptools  # available standard library

REQUIRED = [
    "sklearn",
    "pandas"
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="sprint_1_lambdata-cswizard11",
    version="0.0.1",
    author="cswizard11",
    description=LONG_DESCRIPTION,
    long_description_content="text/markdown",
    url="https://github.com/cswizard11/lambda/tree/main/unit_3/sprint_1_lambdata-cswizard11",
    # how we want to find our REQUIRED packages
    packages=setuptools.find_packages(),
    python_requires=">=3.6",  # what versions of python we are compatibile with
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT Liecense",
    ]
)

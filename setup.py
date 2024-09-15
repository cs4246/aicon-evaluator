from setuptools import setup, find_packages

setup(name="aicon_evaluator",
    version="0.1.0",
    author="Muhammad Rizki Aulia Rahman Maulana",
    author_email="rizki@rizkiarm.com",
    install_requires=[],
    py_packages=["aicon_evaluator"],
    entry_points={
        "console_scripts": [
            "aicon_evaluator=aicon_evaluator:main",
        ],
    },
)

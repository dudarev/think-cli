from setuptools import setup

setup(
    name="t",
    version="0.1.0",
    py_modules=["think-cli"],
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "t = think:cli",
        ],
    },
)

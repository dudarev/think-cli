from setuptools import setup

setup(
    name="t",
    version="0.1.6",
    py_modules=["think-cli"],
    install_requires=[
        "Click==8.1.3",
    ],
    entry_points={
        "console_scripts": [
            "t = think:cli",
        ],
    },
)

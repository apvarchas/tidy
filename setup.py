from setuptools import setup

setup(
    name="tidy-cli",
    version="1.0.0",
    py_modules=["tidy"],
    entry_points={
        "console_scripts": [
            "tidy=tidy:organize"
        ]
    },
)

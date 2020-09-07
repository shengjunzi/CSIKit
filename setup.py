import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="CSIKit",
    version="0.0.1",
    description="Test of CSIKit Deployment",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Gi-z/CSIKit",
    author="Glenn Forbes",
    author_email="gizmoloon@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["CSIKit"],
    include_package_data=True,
    install_requires=["numpy", "matplotlib", "scikit-learn"],
    entry_points={
        "console_scripts": [
            "CSIKit=CSIKit.__main__:main",
        ]
    },
)
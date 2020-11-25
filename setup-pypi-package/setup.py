import setuptools
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg", 
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['somepackage1', 'somepackage2'],  # Optional
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/PackageRepository/Package/issues',
        'Source': 'https://github.com/Project/PackageRepository/tree/develop/Package',
    },
)
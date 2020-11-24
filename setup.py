import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gigsebook", # Replace with your own username
    version="1.0.3",
    author="Gaurav Kumar Yadav",
    author_email="gaurav712@protonmail.com",
    description="a python library to search free eBooks online using Library Genesis's database ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gaurav712/GiGS-eBook",
    packages=setuptools.find_packages(),
    install_requires=[
        'bs4',
        'urllib3',
        'lxml'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
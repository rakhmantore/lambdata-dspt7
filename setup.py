import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iskander.rakhman", # Replace with your own username
    version="0.0.4",
    author="Iskander Rakhmanberdiyev",
    author_email="iskander-r@lambdastudents.com",
    description="a collection of ds utility functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rakhmantore/lambdata-dspt7",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

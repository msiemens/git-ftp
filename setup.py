# coding=utf-8
from setuptools import setup, find_packages

setup(
    name = "git-ftp",
    version = "0.2.7",
    packages = find_packages(),
    scripts = ['GitFTP.py'],
    install_requires = ['GitPython'],

    entry_points = {
        'console_scripts': [
            'git-ftp = GitFTP:main'
        ]
    },

    package_data = {
        'PyGitUp': ['post-recieve']
    },

    # development metadata
    zip_safe = True,

    # metadata for upload to PyPI
    author = "Edward Z. Yang",
    author_email = "ezyang@mit.edu",
    description = "A A quick and efficient way of pushing changed files to a website via FTP",
    license = "MIT",
    keywords = "git ftp",
    url = "https://github.com/msiemens/git-ftp",
    classifiers  = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Version Control",
        "Topic :: Utilities"
    ]
)

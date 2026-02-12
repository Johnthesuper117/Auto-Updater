from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="auto-updator",  # REPLACE THIS with your unique name
    version="1.0.0",
    author="Johnthesuper117",
    author_email="your.email@example.com",
    description="A lightweight GitHub-based auto-updater for Python apps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Johnthesuper117/Auto-Updater",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests",  # Dependency your script needs
    ],
    entry_points={
        'console_scripts': [
            # This allows users to run 'auto-updater' in terminal!
            'auto-updater = auto_updater:do_update', 
        ],
    },
)
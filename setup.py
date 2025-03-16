from setuptools import setup, find_packages

setup(
    name="waview",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "typer[all]",  # Typer for CLI
        "pydub",  # For audio processing
        "pygame",  # For visualization
        "numpy",  # For array processing
    ],
    entry_points={
        "console_scripts": [
            "waview=main:app",  # Expose the Typer app as a CLI command
        ],
    },
    author="Vinicius Novaes",
    author_email="vini2novaes@gmail.com",
    description="An audio visualizer CLI application",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/vcnovaes/audio-visualizer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

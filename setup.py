from setuptools import setup, find_packages

setup(
    name="package_deneme",
    version="0.1.0",
    packages=find_packages(),
    author="Enes Atila",
    description="Python test paketi",
    long_description="Basit bir test paketi",
    long_description_content_type="text/markdown",
    url="https://github.com/enesatila/package_deneme",
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gpuutils",  
    version="0.0.2",
    author="Sefik Ilkin Serengil",
    author_email="serengil@gmail.com",
    description="Gpu Utils: Simple Tool for GPU Analysis and Allocation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/serengil/gpuutils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5.5',
    install_requires=["pandas>=0.23.4"]
)

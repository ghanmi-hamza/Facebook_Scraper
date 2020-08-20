import setuptools





with io.open("README.md", "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setuptools.setup(
    name="Facebook-crawler",
    version = "1.0.0",
    author="Hamza Ghanmi",
    author_email="hamza.ghanmi56@gmail.com",
    license="MIT",
    description="A bot which scrapes the description and posts details from Facebook user's profile",
    long_description_content_type="text/markdown",
    long_description=readme,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: Windows",
    ],
    python_requires=">=3.5",
    install_requires=["selenium==3.141.0","webdriver_manager"],
)

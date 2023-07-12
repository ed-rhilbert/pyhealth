from setuptools import setup, find_packages

setup(
    name="pyhealth",
    version="0.0.1",
    url="<Lien vers les repo, pypi ou la documentation>",
    author="Renan HILBERT",
    author_email="renan.hilbert@gmail.com",
    description="A package to calculate health indicators",
    packages=find_packages(where="src"),
    package_dir={"": "src/"},
    python_requires=">=3.9",
    setup_requires=["wheel"],
    install_requires=[
        # "pandas>=2.0.0",
      ],
)

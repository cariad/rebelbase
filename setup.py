from pathlib import Path

from setuptools import setup

from rebelbase import version

curr_version = version()

readme_path = Path(__file__).parent / "README.md"

with open(readme_path, encoding="utf-8") as f:
    long_description = f.read()

classifiers = [
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Typing :: Typed",
]

if "a" in curr_version:
    classifiers.append("Development Status :: 3 - Alpha")
elif "b" in curr_version:
    classifiers.append("Development Status :: 4 - Beta")
else:
    classifiers.append("Development Status :: 5 - Production/Stable")

classifiers.sort()

setup(
    author="Cariad Eccleston",
    author_email="cariad@cariad.earth",
    classifiers=classifiers,
    description="Recruit numbers to any base",
    include_package_data=True,
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="rebelbase",
    packages=[
        "rebelbase",
    ],
    package_data={
        "rebelbase": ["py.typed"],
    },
    project_urls={
        "Documentation": "https://rebelbase.dev",
        "Funding": "https://github.com/sponsors/cariad",
        "Issues": "https://github.com/cariad/rebelbase/issues",
        "Source": "https://github.com/cariad/rebelbase",
    },
    python_requires=">=3.9",
    url="https://rebelbase.dev",
    version=curr_version,
)

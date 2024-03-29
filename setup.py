from setuptools import setup


def get_description():
    with open("README.rst") as file:
        return file.read()


setup(
    name="Lazify",
    version="0.4.0",
    url="https://github.com/Refty/lazify",
    license="BSD",
    author="Guillaume Gelin",
    author_email="guillaume@refty.co",
    description="Lazify all the things!",
    long_description=get_description(),
    py_modules=["lazify"],
    platforms="any",
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)

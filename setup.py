from setuptools import setup


def get_description():
    with open("README.rst") as file:
        return file.read()


setup(
    name="Lazify",
    version="0.1.2",
    url="https://github.com/numberly/lazify",
    license="MIT",
    author="Guillaume Gelin",
    author_email="ramnes@1000mercis.com",
    description="Lazify all the things!",
    long_description=get_description(),
    py_modules=["lazify"],
    include_package_data=True,
    zip_safe=False,
    platforms="any",
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)

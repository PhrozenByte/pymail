from distutils.core import setup

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="pymail",
    version="0.0.1",
    description="Simple Python script to synchroniously send emails via SMTP. " +
        "It is often used on satellite systems without a fully-featured MTA.",
    long_description=readme,
    author="Daniel Rudolf",
    author_email="pymail@daniel-rudolf.de",
    url="https://github.com/PhrozenByte/pymail",
    license=license,
    py_modules=[ "pymail" ],
    scripts=[ "pymail" ]
)

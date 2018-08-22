from setuptools import setup

with open("README", "r") as fh:
    long_description = fh.read

setup\
(
    name                            = 'pyfractals',
    version                         = '0.1',
    description                     = 'A library to generate cartesian coordinates for fractals along with plotting capability.',
    long_description                = long_description,
    long_description_content_type   = "text/markdown",
    url                             = 'https://github.com/kirit93/Fractals',
    author                          = 'kirit93',
    author_email                    = 'kirit.thadaka@gmail.com',
    licence                         = 'MIT',
    packages                        = ['pyfractals'],
    zip_safe                        = False
)
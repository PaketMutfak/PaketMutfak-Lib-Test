from setuptools import find_packages, setup

__version__ = "1.1.28"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='paketmutfak',
    version=__version__,
    author='Paket Mutfak',
    author_email='dev@paketmutfak.com.tr',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/PaketMutfak/PaketMutfak-Lib-Test',
    project_urls={
        "Bug Tracker": "https://github.com/PaketMutfak/PaketMutfak-Lib-Test/issues"
    },
    license='MIT',
    packages=find_packages(),
    install_requires=['requests',
                      'boto3',
                      'mysql-connector',
                      'uuid',
                      'datetime',
                      'iso8601',
                      'slugify',
                      'PyJWT',
                      'beartype',
                      'flask'],
)

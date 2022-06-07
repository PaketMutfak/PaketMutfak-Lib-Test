import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='paketmutfak',
    version='1.0.0',
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
    packages=['utils', 'db'],
    install_requires=['requests',
                      'boto3',
                      'mysql-connector',
                      'uuid',
                      'random',
                      'datetime',
                      'iso8601',
                      'slugify',
                      're',
                      'PyJWT',
                      'math'],
)



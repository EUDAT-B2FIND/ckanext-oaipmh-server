from setuptools import setup, find_packages

version = '0.9.0'

setup(
    name='ckanext-oaipmh-server',
    version=version,
    description="OAI-PMH server for CKAN",
    long_description="""\
        """,
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='EUDAT-B2FIND',
    author_email='https://www.eudat.eu/support-request',
    url='http://b2find.eudat.eu/',
    license='AGPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.oaipmh'],
    include_package_data=True,
    zip_safe=False,

    entry_points="""
        [ckan.plugins]
        oaipmh=ckanext.oaipmh.plugin:OAIPMHPlugin
        """,
)

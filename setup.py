from setuptools import setup, find_packages

setup(
    name='reportportal-client',
    packages=find_packages(),
    version='2.5.0',
    description='Python client for ReportPortal',
    author='Artsiom Tkachou',
    author_email='artsiom_tkachou@epam.com',
    url='https://github.com/EPAMReportPortal/ReportPortal-Python-Client',
    download_url='https://github.com/EPAMReportPortal/ReportPortal-Python-Client/tarball/2.5.0',
    keywords=['testing', 'reporting', 'reportportal'],
    classifiers=[],
    install_requires=["requests"],
)

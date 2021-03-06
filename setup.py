from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='hr',
    version='1.0.0',
    description='Command line user export utility',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Davis Damian',
    author_emai='ddamian.sbp@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
    entry_points={'console_scripts': 'hr=hr.cli:main'},
)
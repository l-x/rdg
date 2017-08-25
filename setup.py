from setuptools import setup
import io
import sys
import rdg

repo_url='http://github.com/l-x/rdg'

with io.open('README.rst', 'r', encoding='utf-8') as readme_file:
    readme = readme_file.read()

if sys.argv[-1] == 'readme':
    print(readme)
    sys.exit()

requirements = [
    'unidecode',
    'jinja2'
]

setup(
    name='rdg',
    version=rdg.version,
    description='Random data generator',
    long_description=readme,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3 :: Only',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Software Development',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Testing :: Traffic Generation',
    ],
    keywords='rdg template random list data generator Jinja2',
    url=repo_url,
    author='l-x',
    author_email='l-x+github@mailbox.org',
    license='MIT',
    install_requires=requirements,
    tests_require=['mypy', 'nose2'],
    entry_points={
        'console_scripts': ['rdg=rdg.cli:main'],
    },
    include_package_data=True,
    zip_safe=False,
    test_suite='nose2.collector.collector',
    packages=['rdg'],
    package_dir={'rdg': 'rdg/'},
    package_data={'rdg': ['vocabulary/*.json']},
    download_url="{}/archive/{}.tar.gz".format(repo_url, rdg.version)
)

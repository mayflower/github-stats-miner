from setuptools import setup, find_packages

config = {
    'description': 'Github Statistics Miner and Graphing',
    'author': 'Robin Gloster',
    'author_email': 'mail@glob.in',
    'version': '0.1',
    'install_requires': [
        'github3.py',
    ],
    'entry_points': {
        'console_scripts': [
            'gh_miner = gh_miner:main',
        ]
    },
    'packages': ['gh_miner'],
    'packages': find_packages(),
    'name': 'gh_miner',
}

setup(**config)

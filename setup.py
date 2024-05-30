from setuptools import setup, find_packages

setup(
    name='featurify',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A brief description of the Featurify library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/featurify',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'streamlit',
    ],
    entry_points={
        'console_scripts': [
            'featurify=featurify.cli:main',
        ],
    },
)

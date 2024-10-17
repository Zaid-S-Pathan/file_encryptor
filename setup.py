from setuptools import setup, find_packages

setup(
    name='my_encryption_package',
    version='0.1',
    packages=find_packages(),
    install_requires=['cryptography'],  # Dependencies
    author='Your Name',
    author_email='your.email@example.com',
    description='A file encryption package',
    url='https://github.com/yourusername/my_encryption_package',  # Optional GitHub URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)

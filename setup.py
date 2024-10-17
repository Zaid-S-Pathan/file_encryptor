from setuptools import setup, find_packages

setup(
    name='my_encryption_package',
    version='0.1',
    packages=find_packages(),
    install_requires=['cryptography'],  # Dependencies
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple file encryption package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_encryption_package',  # Optional GitHub URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

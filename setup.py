from setuptools import find_packages, setup

with open("README.MD", "r") as f:
    long_description = f.read()

setup(
    name='hisql',
    version='0.0.2',
    packages=find_packages(include=['hisql']),
    include_package_data=True,
    zip_safe=False,
    description='纯SQL操作数据库',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/buf1024/hisql",
    platform="any",
    install_requires=[
        'pugsql',
        'pandas'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)

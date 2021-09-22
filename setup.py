from setuptools import find_packages, setup

setup(
    name='hisql',
    version='0.0.1',
    packages=find_packages(include=['hisql']),
    include_package_data=True,
    zip_safe=False,
    platform="any",
    install_requires=[
        'pugsql',
        'pandas'
    ],
)

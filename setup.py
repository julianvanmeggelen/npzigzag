from setuptools import find_packages, setup

setup(
    name='npzigzag',
    packages=find_packages(include=['npzigzag']),
    version='0.1.0',
    description='Vanilla numpy implementation of zigzag indicator.',
    author='Julian van Meggelen',
    license='MIT',
    install_requires = [
        'numpy==1.19.1',
        'pandas==1.1.0'
        ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==6.2.5'],
    test_suite='npzigzag_tests'
)

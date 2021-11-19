from setuptools import find_packages, setup

setup(
    name='npzigzag',
    packages=find_packages(include=['npzigzag']),
    version='0.2',
    description='Vanilla numpy implementation of zigzag indicator.',
    long_description="readme",
    long_description_content_type="text/markdown",
    author='Julian van Meggelen',
    license='MIT',
    install_requires = [
        'numpy==1.19.1',
        'pandas==1.1.0'
        ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==6.2.5'],
    test_suite='npzigzag_tests',
    author_email = 'julianvanmeggelen@icloud.com',      
    url = 'https://github.com/julianvanmeggelen/npzigzag',  
    download_url = 'https://github.com/julianvanmeggelen/npzigzag/archive/refs/tags/v01.tar.gz',    # I explain this later on
    keywords = ['zigzag', 'zigzag indicator'],   
    classifiers=[
        'Development Status :: 3 - Alpha',      #  "3 - Alpha", "4 - Beta" or "5 - Production/Stable" 
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   #license
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)

from setuptools import setup, find_packages

setup(
    name='github_issue_fetcher',  
    version='0.1',
    packages=find_packages(where='Issue_Manager'),  # Specify the package directory correctly
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'github_issue_fetcher=client:client_app',  
        ],
    },
    include_package_data=True,  # Include other files specified in MANIFEST.in (if used)
    python_requires='>=3.6',  # Specify the minimum Python version required
)

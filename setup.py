from setuptools import setup, find_packages

setup(
    name="github-user-activity",
    version="0.1.0",
    description="A CLI tool that fetches a Github user's recent activities by using the Github API.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="NguyenDong",
    author_email="doannguyendong1808@gmail.com",
    url="https://github.com/ndongdoan/github-user-activity",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    entry_points = {
        "console_scripts": [
            "get=github_api_request.script:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    python_requires=">=3.6",
)
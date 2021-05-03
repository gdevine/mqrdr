import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='mqrdr',  
     version='0.2',
     author="Gerry Devine",
     author_email="gerry.devine@mq.edu.au",
     description="Python 3 library, leveraging off of the Figshare API, for programmatic interaction with the Macquarie University Research Data Repository",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://gitlab.com/gdevine/mqrdr",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     install_requires=['requests'],
     python_requires='>=3'
 )
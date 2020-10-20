from setuptools import setup, find_packages
from os.path import join, dirname
import helloworld

setup(
    name='hellonj1902',
    version=helloworld.__version__,
    packages=find_packages(),
    license='MIT',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    long_description_content_type="text/markdown",
    entry_points={
    'console_scripts':
        [
        'helloworld = helloworld.core:print_message',
        'serve = helloworld.web:run_server',
        ]
    },   # Create an executable with the name helloworld.
    install_requires=[
        'Flask'
    ], # whatever modules installed using pip used in project will be passed here
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
],
)

## When running the setup script, it will create a folder with the extension .egg-info.
#  If you make changes to your MANIFEST.in file, you should delete this folder. It contains a file named SOURCES.txt
#  which contains all the file in the package. If you remove files from your manifest, the will  only disappear when 
#  that file is changes as well. So the easiest way is to delete the egg-info folder and let the setup script re-create it!
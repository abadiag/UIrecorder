import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='UIrecorder',
    version='1.0',
    packages=['UIrecorder'],
    url='https://github.com/abadiag/UIrecorder',
    author='Albert Badia',
    author_email='abgsoftdevelop@gmail.com',
    license='CopyRight 2020',
    description=README,
    install_requires=[
        'pynput',
        'pyautogui',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={'console_scripts': ['Package = UIrecorder.__init__']}
)

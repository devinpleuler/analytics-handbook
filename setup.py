from distutils.core import setup

# Encoding error fix on Windows: https://stackoverflow.com/questions/49640513/unicodedecodeerror-charmap-codec-cant-decode-byte-0x9d-in-position-x-charac
setup(
    name='AnalyticsHandbook',
    version='0.2dev',
    packages=['soccerutils', ],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md', encoding='utf8').read(),
)

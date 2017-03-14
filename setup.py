from distutils.core import setup

setup(name='minivoco',
      version='0.0.1',
      description='Simple vocoder prototype module',
      author='Ryan Birmingham',
      author_email='birm@rbirm.us',
      url='http://rbirm.us',
      classifiers=['Topic :: Multimedia :: Sound/Audio :: Sound Synthesis',
                   'Topic :: Multimedia :: Sound/Audio :: Speech'
                   'Topic :: Multimedia :: Sound/Audio',
                   'Intended Audience :: Information Technology',
                   'Development Status :: 1 - Planning',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: System :: Hardware',
                   'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'],
      long_description=open('README.md', 'r').read(),
      packages=['minivoco'],
      )

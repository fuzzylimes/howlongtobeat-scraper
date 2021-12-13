from setuptools import setup

setup(name='hltb_time_scraper',
      version='0.2',
      description='Tool to scrape the completion times for games from howlongtobeat.com',
      url='https://github.com/fuzzylimes/howlongtobeat-scraper',
      author='fuzzylimes',
      license='MIT',
      packages=['hltbScraper'],
      install_requires=[
          'beautifulsoup4==4.6.0',
          'certifi==2017.11.5',
          'chardet==3.0.4',
          'idna==2.6',
          'lxml==4.6.5',
          'pyOpenSSL==19.1.0',
          'requests==2.20.0',
          'urllib3==1.24.2'
      ],
      zip_safe=False)

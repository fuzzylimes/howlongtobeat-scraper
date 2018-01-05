from setuptools import setup

setup(name='hltb_time_scraper',
      version='0.1',
      description='Tool to scrape the completion times for games from howlongtobeat.com',
      url='https://github.com/fuzzylimes/howlongtobeat-scraper',
      author='fuzzylimes',
      license='MIT',
      packages=['hltbScraper'],
      install_requires=[
          'beautifulsoup4==4.6.0',
          'lxml==4.1.1',
          'requests==2.18.4'
      ],
      zip_safe=False)
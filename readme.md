Crawl's the entire Twitter timeline of any user with a public profile and stores it in a folder identical
to the users Twitter-Handle (@Username).

# Prequesites

1. [Probably ffmpeg installed (not sure)](https://www.ffmpeg.org).
2. [Python 3.8.](https://www.python.org/downloads/)
3. [Pip](https://pip.pypa.io/en/latest/installing/)

# Setup

1. Clone or download this repository.
2. [Create and activate a virtual environment](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/) within your local copy's directory.
3. Run `pip install -r requirements.txt`
4. Run `python crawler.py -user user_name -destination-directory directory`
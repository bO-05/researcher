import os
from dotenv import load_dotenv
load_dotenv()

# API
# Key to access the OpenAI API
OPENAI_KEY = os.environ.get('OPENAI_KEY')
# Maximum number of tokens
OPENAI_TOKEN_MAX = 512

# Search
# Minimum length for valid search query
QUERY_MIN_LENGTH = 10
# Number of results to search for
RESULT_COUNT = 10
# Minimum number of valid search results
MIN_RESULTS = 5
# Maximum processes to use when scraping results
MAX_PROCESSES = 10
# Max time to wait when scraping results
RESULT_TIMEOUT = 5
# Search method
# SEARCH_METHOD = "api"  # "scrape" or "api"
SEARCH_METHOD = "scrape"  # "scrape" or "api"

# Google Custom Search
# Only used when SEARCH_METHOD is "api"
# Google custom search api key
# SEARCH_KEY = ""
SEARCH_KEY = os.environ.get('GOOGLE_SEARCH_API_KEY')
# Google custom search engine id
# SEARCH_ID = ""
SEARCH_ID = os.environ.get('GOOGLE_SEARCH_ENGINE_ID')
# Country to search from
COUNTRY = "us"
# Google custom search url
SEARCH_URL = "https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&q={query}&start={start}&num=10&gl=" + COUNTRY

# Filtering
# Maximum number of tracker URLs allowed in a site (rejects sites with more)
MAX_TRACKER_URLS = 2

# Parsing
# Language to use to parse results
LANGUAGE = "en"
# Maximum length in words for context chunks to be used in prompt
CHUNK_MAX_LENGTH = 256
# Minimum length in words for context chunks to be used in prompt
CHUNK_MIN_LENGTH = 128
# Number of chunks to use when generating prompt
CHUNK_LIMIT = 5

# Display
# Maximum number of characters in a chunk to display
CHUNK_DISPLAY_CHARS = 500


if os.path.exists("private.py"):
    from private import *

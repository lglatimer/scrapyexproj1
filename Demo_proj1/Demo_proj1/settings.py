# -*- coding: utf-8 -*-

# Scrapy settings for Demo_proj1 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'Demo_proj1'

SPIDER_MODULES = ['Demo_proj1.spiders']
NEWSPIDER_MODULE = 'Demo_proj1.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Demo_proj1 (+http://www.yourdomain.com)'


# Broad crawl defaults from scrapy documentation
#  http://doc.scrapy.org/en/latest/topics/broad-crawls.html
CONCURRENT_REQUESTS = 100
LOG_LEVEL = 'DEBUG'
COOKIES_ENABLED = False
RETRY_ENABLED = False
DOWNLOAD_TIMEOUT = 15
REDIRECT_ENABLED = False
AJAXCRAWL_ENABLED = True

# Additional broad crawl settings to conserve resources
CONCURRENT_REQUESTS_PER_DOMAIN = 4
DEPTH_LIMIT = 4

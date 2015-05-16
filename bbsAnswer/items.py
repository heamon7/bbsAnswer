# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BbsanswerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    questionLink = scrapy.Field()
    answerPageNum = scrapy.Field()
    floorNumList = scrapy.Field()
    answerPositionList = scrapy.Field()
    userIdList = scrapy.Field()
    userImgLinkList = scrapy.Field()
    userNameList = scrapy.Field()
    userClassList = scrapy.Field()
    userQuestionCountList = scrapy.Field()
    userScoreList = scrapy.Field()
    answerTimeList = scrapy.Field()
    answerIpList = scrapy.Field()
    answerContentList = scrapy.Field()

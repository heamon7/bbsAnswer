# -*- coding: utf-8 -*-
import scrapy
from scrapy.shell import inspect_response
from scrapy.http import Request,FormRequest

import re

import leancloud
from leancloud import Object
from leancloud import LeanCloudError
from leancloud import Query

from scrapy import log
from datetime import datetime
from scrapy.exceptions import DropItem

from  bbsAnswer.items import BbsanswerItem

class AnswererSpider(scrapy.Spider):
    name = "answerer"
    baseUrl = "http://bbs.byr.cn"
    allowed_domains = ["bbs.byr.cn"]
    start_urls = (
        'http://bbs.byr.cn/',
    )

    def __init__(self):
        leancloud.init('mctfj249nwy7c1ymu3cps56lof26s17hevwq4jjqeqoloaey', master_key='ao6h5oezem93tumlalxggg039qehcbl3x3u8ofo7crw7atok')

        Questions = Object.extend('Questions')
        query = Query(Questions)
        curTime = datetime.now()
        query.exists('questionLink')
        query.less_than('createdAt',curTime)
        questionCount = query.count()


        print "questionCounts: %s" %str(questionCount)
        queryLimit = 500
        queryTimes = questionCount/queryLimit + 1
        self.urls = []

        for index in range(queryTimes):
            query = Query(Questions)
            query.exists('questionLink')
            query.less_than('createdAt',curTime)
            query.descending('createdAt')
            query.limit(queryLimit)
            query.skip(index*queryLimit)
            query.select('questionLink')
            quesRet = query.find()
            for ques in quesRet:
                self.urls.append(self.baseUrl + ques.get('questionLink'))
        pass


    def start_requests(self):
        print "start_requests ing ......"
        self.urls = ['http://bbs.byr.cn/article/Python/2735','http://bbs.byr.cn/article/Python/2145']
        print self.urls
        for url in self.urls:
            yield Request(url,callback = self.parse)

    def parse(self, response):
        #inspect_response(response,self)
        try:
            totalPageNum = int(response.xpath('//div[@class="t-pre-bottom"]//ul[@class="pagination"]//ol[@class="page-main"]/li[last()-1]/a/text()').extract()[0])
        except:
            totalPageNum = int(response.xpath('//div[@class="t-pre-bottom"]//ul[@class="pagination"]//ol[@class="page-main"]/li[last()]/a/text()').extract()[0])

        for index in range(1,totalPageNum+1):
            yield Request(response.url+'?p=' +str(index),callback = self.parseAnswer)
      #  print item['sectionListLink']

    def parseAnswer(self,response):
        item = BbsanswerItem()

        content = response.xpath('//div[@class="b-content corner"]')
        item['questionLink'] = '/article'+re.split('article/(\w*/\d*)',response.url)[1]
        item['answerPageNum'] = re.split('p=(\d*)',response.url)[1]

        item['floorNumList'] = content.xpath('//a[@name]/@name').extract()
        item['answerPositionList'] = content.xpath('//div[@class="a-wrap corner"]//tr[@class="a-head"]//span[@class="a-pos"]/text()').extract()
        item['userIdList'] = content.xpath('//div[@class="a-wrap corner"]//tr[@class="a-head"]//span[@class="a-u-name"]//text()').extract()

        item['userImgLinkList'] = content.xpath('//div[@class="a-wrap corner"]//tr[@class="a-body"]//div[@class="a-u-img"]/img/@src').extract()
        item['userNameList'] = content.xpath('//div[@class="a-wrap corner"]//tr[@class="a-body"]//div[@class="a-u-uid"]/text()').extract()
        item['userClassList'] = content.xpath('//div[@class="a-wrap corner"]//tr[@class="a-body"]//dl[@class="a-u-info"]//dd[1]/text()').extract()
        item['userQuestionCountList'] = content.xpath('//div[@class="a-wrap corner"]//tr[@class="a-body"]//dl[@class="a-u-info"]//dd[2]/text()').extract()
        item['userScoreList'] = content.xpath('//div[@class="a-wrap corner"]//tr[@class="a-body"]//dl[@class="a-u-info"]//dd[3]/text()').extract()

        item['answerTimeList'] = []
        item['answerIpList'] =[]
        item['answerContentList'] = []

        for index ,sel in enumerate(item['floorNumList']):
            answerTime = content.xpath('//div[@class="a-wrap corner"]'+'['+str(index+1)+']'+'//tr[@class="a-body"]//td[@class="a-content"]//div//text()')[2].re('(\w*\s*\w*\s*\d*\s*\d*:\d*:\d*\s*\d*)')[0]
            item['answerTimeList'].append(answerTime)
            answerIp = content.xpath('//div[@class="a-wrap corner"]'+'['+str(index+1)+']'+'//tr[@class="a-body"]//td[@class="a-content"]//div//text()')[-1].re('(\d*\.\d*\.\d*\.\*)')[0]
            item['answerIpList'].append(answerIp)
            answerContent = content.xpath('//div[@class="a-wrap corner"]'+'['+str(index+1)+']'+'//tr[@class="a-body"]//td[@class="a-content"]//div//text()')[3:-4].extract()
            item['answerContentList'].append(answerContent)

        return item

# content.xpath('//div[@class="a-wrap corner"]'+'['+str(index+1)+']'+'//tr[@class="a-body"]//td[@class="a-content"]//div//text()')[3:-4].extract()
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import leancloud
from leancloud import Object
from leancloud import LeanCloudError
from leancloud import Query
from scrapy import log
from scrapy.exceptions import DropItem

class AnswerPipeline(object):
    def __init__(self):
        leancloud.init('mctfj249nwy7c1ymu3cps56lof26s17hevwq4jjqeqoloaey', master_key='ao6h5oezem93tumlalxggg039qehcbl3x3u8ofo7crw7atok')
        pass
    def process_item(self, item, spider):

        Answers = Object.extend('Answers')
        Users = Object.extend('Users')


        for index ,ques in enumerate(item['floorNumList']):
            answer = Answers()
            user = Users()
            queryAnswer = Query(Answers)
            queryUser = Query(Users)
            queryAnswer.equal_to('questionLink',item['questionLink'])
            queryAnswer.equal_to('userId',item['userIdList'][index])
            queryAnswer.equal_to('answerTime',item['answerTimeList'][index])
            try:
                if queryAnswer.find():
                    pass
                else:
                    answer.set('questionLink',item['questionLink'])
                    answer.set('answerPageNum',item['answerPageNum'])

                    answer.set('floorNum',item['floorNumList'][index])
                    answer.set('answerPosition',item['answerPositionList'][index])

                    answer.set('userId',item['userIdList'][index])
                    answer.set('answerTime',item['answerTimeList'][index])
                    answer.set('answerIp',item['answerIpList'][index])
                    answer.set('answerContent',item['answerContentList'][index])
                    try:
                        answer.save()

                    except LeanCloudError,e:
                        print e
            except LeanCloudError,e:
                print e

            queryUser.equal_to('userId',item['userIdList'][index])
            try:
                if queryUser.find():
                    pass
                else:
                    user.set('userId',item['userIdList'][index])
                    user.set('userImgLink',item['userImgLinkList'][index])
                    user.set('userName',item['userNameList'][index])
                    user.set('userClass',item['userClass'][index])
                    user.set('userQuestionCount',item['userQuestionCountList'][index])
                    user.set('userScore',item['userScore'][index])
                    try:
                        user.save()
                    except LeanCloudError,e:
                        print e
            except LeanCloudError,e:
                print e



        return item
        #DropItem()

# questionLink
# answerPageNum
#
# floorNumList
# answerPositionList
# userIdList

# userImgLinkList
# userNameList
# userClassList
# userQuestionCountList
# userScoreList

# answerTimeList
# answerIpList
# answerContent

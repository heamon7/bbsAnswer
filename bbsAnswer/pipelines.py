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

    def process_item(self, item, spider):

#         Answers = Object.extend('Answers')
#         answer = Object.extend('Answers')
# # questionLink
# # answerPageNum
# #
# # floorNumList
# # answerPositionList
# # userIdList
# # userImgLinkList
# # userNameList
# # userClassList
# # userQuestionCountList
# # userScoreList
# # answerTimeList
# # answerIpList
# # answerContent
#
#         for index ,ques in enumerate(item['floorNumList']):
#             answer = Answers()
#             answerInfo = QuestionInfo()
#             query = Query(Answers)
#             queryInfo = Query(QuestionInfo)
#             query.equal_to('questionLink',item['questionLinkList'][index])
#             try:
#                 if query.find():
#                     pass
#                 else:
#                     question.set('boardLink',item['boardLink'])
#                     question.set('pageNum',item['pageNum'])
#                     question.set('questionLink',item['questionLinkList'][index])
#                     question.set('questionName',item['questionNameList'][index])
#                     question.set('questionReleaseDatetime',item['questionReleaseDatetimeList'][index])
#                     question.set('questionAuthorLink',item['questionAuthorLinkList'][index])
#                     question.set('questionAuthorId',item['questionAuthorIdList'][index])
#                     try:
#                         question.save()
#
#                     except LeanCloudError,e:
#                         print e
#             except LeanCloudError,e:
#                 print e
#                # query.equal_to('questionReplyNum',item['questionReplyNumList'][index])
#             queryInfo.equal_to('questionLink',item['questionLinkList'][index])
#             queryInfo.equal_to('questionReplyCount',int(item['questionReplyCountList'][index]))
#             try:
#                 if queryInfo.find():
#                     pass
#                 else:
#                     questionInfo.set('boardLink',item['boardLink'])
#                     questionInfo.set('pageNum',item['pageNum'])
#                     questionInfo.set('questionLink',item['questionLinkList'][index])
#                     questionInfo.set('questionType',item['questionTypeList'][index])
#                     questionInfo.set('questionName',item['questionNameList'][index])
#                     questionInfo.set('questionReleaseDatetime',item['questionReleaseDatetimeList'][index])
#                     questionInfo.set('questionAuthorLink',item['questionAuthorLinkList'][index])
#                     questionInfo.set('questionAuthorId',item['questionAuthorIdList'][index])
#                     questionInfo.set('questionReplyCount',int(item['questionReplyCountList'][index]))
#                     questionInfo.set('questionLastReplyLink',item['questionLastReplyLinkList'][index])
#                     questionInfo.set('questionLastReplyDatetime',item['questionLastReplyDatetimeList'][index])
#                     questionInfo.set('questionLastReplyIdLink',item['questionLastReplyIdLinkList'][index])
#                     questionInfo.set('questionLastReplyId',item['questionLastReplyIdList'][index])
#
#
#                     try:
#                         questionInfo.save()
#
#                     except LeanCloudError,e:
#                         print e
#             except LeanCloudError,e:
#                 print e



        return item
        #DropItem()

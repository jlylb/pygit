#!/usr/bin/env python
#coding=utf8
"""
# Author: litc
# Created Time : 2015/10/29 14:01:15
  Last Modified: 2015/10/29 16:58:41
# File Name: TcSpider.py
# Description:

"""
import scrapy,uuid,json,codecs
class TcSpider(scrapy.Spider):
    name="Tc"
    allowed_domains=["tencent.com"]
    start_urls=[
        "http://hr.tencent.com/position.php?&start=0#a"
    ]

    def parse(self,response):
        linejobs = []
        for lines in response.xpath("//table[@class='tablelist']/tr[@class='even' or @class='odd']"):
            linejobs.append([line.extract() for line in lines.xpath(".//td[position()>1]/text()|.//td[1]/a/text()|.//td[1]/a/attribute::href")])
        print linejobs
        fname = uuid.uuid1().hex + '.json'
        with codecs.open(fname,'wb',encoding='utf-8') as f:
            f.write(json.dumps(linejobs,ensure_ascii=False))



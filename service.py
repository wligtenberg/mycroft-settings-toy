from skill import skill
from skill1 import skill1
from skill2 import skill2

import sys
# from lxml.html import builder as E
# import lxml
import xml.etree.cElementTree as ET

class service:
    config_xmls = []

    def __init__(self):
        s1 = skill1()
        self.config_xmls.append(s1.define_configuration())
        s2 = skill2()
        self.config_xmls.append(s2.define_configuration())
        self.write_html()

    def write_html(self):
        # html = E.HTML(lang = 'en')
        # head = E.HEAD(
        #     E.META(charset = 'utf-8'),
        #     E.META(http-equiv = 'X-UA-Compatible')
        # )
        # html.append(head)
        # print lxml.html.tostring(html)



        html = ET.Element('html', lang = 'en')
        head = ET.SubElement(html, 'head')
        meta = ET.SubElement(head, 'meta', charset = 'utf-8')
        meta = ET.SubElement(head, 'meta')
        meta.set('http-equiv', 'X-UA-Compatible')
        meta.set('content', 'IE=edge')
        meta = ET.SubElement(head, 'meta', name = 'viewport', content = 'width=device-width, initial-scale=1')
        title = ET.SubElement(head, 'title')
        title.text = 'Mycroft setting page'
        link = ET.SubElement(head, 'link', href = 'bootstrap/css/bootstrap.min.css', rel = 'stylesheet')
        body = ET.SubElement(html, 'body')
        script = ET.SubElement(body, 'script', src = 'https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js')
        script = ET.SubElement(body, 'script', src = 'bootstrap/js/bootstrap.min.js')
        for xml in self.config_xmls:
            body.append(xml.xml)
        doc = ET.ElementTree(html)
        doc.write('test.html', method = "html")

if __name__ == '__main__':
    s = service()

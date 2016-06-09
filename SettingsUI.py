import xml.etree.cElementTree as ET

class SettingsUI:
    def __init__(self):
        pass

    def settings():
        node = ET.Element('foo')
        node.text = 'bar'
        doc = ET.ElementTree(node)
        return doc

class BootstrapPanel:
    xml = None

    def __init__(self, title):
        panel = ET.Element('div')
        panel.set('class', 'panel panel-default')
        heading = ET.Element('div')
        heading.set('class', 'panel-heading')
        t = ET.Element('h3')
        t.text = title
        t.set('class', 'panel-title')
        heading.append(t)
        body = ET.Element('div')
        body.set('class', 'panel-body')
        panel.append(heading)
        panel.append(body)
        self.xml = panel

    def append(self, object):
        self.xml.append(object.xml)

class BootstrapInputGroup:
    xml = None

    def __init__(self, config_option):
        ig = ET.Element('div')
        ig.set('class', 'input-group')
        i =  ET.Element('input', type = 'text', placeholder=config_option)
        ig.append(i)
        self.xml = ig

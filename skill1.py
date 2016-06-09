from skill import skill
from SettingsUI import *

class skill1(skill):
    def __init__(self):
        print 'skill1 called'

    def define_configuration(self):
        panel = BootstrapPanel('Skill 2 configuration options')
        panel.append(BootstrapInputGroup('username'))
        return(panel)

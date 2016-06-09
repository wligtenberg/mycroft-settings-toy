from skill import skill
from SettingsUI import *

class skill2(skill):
    def __init__(self):
        print 'skill2 called'

    def define_configuration(self):
        panel = BootstrapPanel('Skill 2 configuration options')
        panel.append(BootstrapInputGroup('username'))
        return(panel)

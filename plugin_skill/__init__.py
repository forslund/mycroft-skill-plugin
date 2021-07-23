# Copyright 2021 Åke Forslund
#
# This test plugin is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This module is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler

class PluginSkill(MycroftSkill):
    @intent_handler(IntentBuilder('').require('PluginKeyword'))
    def handle_plugin_intent(self, message):
        self.speak_dialog("plugin")


def create_skill():
    return PluginSkill()

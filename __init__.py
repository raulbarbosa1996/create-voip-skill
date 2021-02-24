from mycroft import MycroftSkill, intent_file_handler


class CreateVoip(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('voip.create.intent')
    def handle_voip_create(self, message):
        self.speak_dialog('voip.create')


def create_skill():
    return CreateVoip()





class event:
    def __init__(self, name_event, date_event, link_event=None):
        self.name_event = name_event
        self.date_event = date_event
        self.link_event = link_event

class busy:
    def __init__(self, id_user):
        self.id_user = id_user
        self.events = []

    def add_event(self, event):
        self.events.add(event)

    def get_today(self):
        if len(self.events) == 0:
            return "Прости брат, ты свободен как Куба)"
        else:
            return "Всего событий " + str(len(self.events))




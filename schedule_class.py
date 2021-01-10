import datetime as dt
import json



class Event:
    week = ['понедельник', 'вторник', 'среда', 'четверг', 'суббота', 'воскресенье']

    def encode_time(t):
        temp = t.split(":")
        return int(temp[0]) * 60 + int(temp[1])

    def time_interval(t1, t2):
        #print(t1.time, t2.time)
        t1_ = Event.encode_time(t1.time) + t1.duration
        t2_ = Event.encode_time(t2.time)
        return max(0, t2_ - t1_)


    def __init__(self, name, date, time, duration = 60, link=None, comment=None, period=[]):
        self.name = name
        self.date = date
        self.time = time
        self.link = link
        self.duration = duration
        self.period = period
        self.comment = comment

    def __str__(self):
        return str(self.__dict__)



class Busy:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def filter_day(self, day):
        rez = []
        for e in self.events:
            date_busy = dt.datetime.strptime(e.date, '%Y-%m-%d').date()
            date_user = day.toPyDate()
            if date_busy == date_user:
                rez.append(e)
        rez.sort(key=(lambda x: x.time))
        return rez

    def get_today(self, day=None):
        if day is None:
            day = dt.date.today()
        temp_events = self.filter_day(day)
        return temp_events

    def encode_json(self):
        return [i.__dict__ for i in self.events]



    def save(self):
        try:
            with open("calendar.json", "w", encoding="utf-8") as file:
                #json.dump(self, file, default=encode_json)
                json.dump(self.encode_json(), file)
        except:
            print("Не удалось записать в файл")

    def load(self):
        try:
            with open("calendar.json", "r", encoding="utf-8") as file:
                #json.dump(self, file, default=encode_json)
                temp = json.load(file)
                self.events = [Event(t['name'], t['date'], t['time'], t['duration'], t['link'], t['comment'], t['period']) for t in temp]
                #print(temp)
        except:
            print("Не удалось считать из файла")

    def __str__(self):
        return "\nВсе события:\n"+"\n".join([str(e) for e in self.events])

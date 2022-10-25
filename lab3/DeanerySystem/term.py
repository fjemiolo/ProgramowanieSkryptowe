from day import Day


class Term(object):

    def __init__(self, day: Day, hour, minute):
        self.hour = hour
        self.minute = minute
        self.duration = 90
        self.__day = day

    def __str__(self):
        return "%s %d:%d [%d]" % (self.__day.readable(), self.hour, self.minute, self.duration)

    def earlierThan(self, term):
        if self.__day.difference(term.__day) > 0:
            return True
        elif self.__day.difference(term.__day) == 0:
            if (self.hour < term.hour) or (self.hour == term.hour and self.minute < term.minute):
                return True
        return False

    def laterThan(self, term):
        if self.__day.difference(term.__day) < 0:
            return True
        elif self.__day.difference(term.__day) == 0:
            if (self.hour > term.hour) or (self.hour == term.hour and self.minute > term.minute):
                return True
        return False

    def equals(self, term):
        if (self.__day == term.__day) and (self.hour == term.hour) and (self.minute == term.minute) and (
                self.duration == term.duration):
            return True
        return False

from enum import Enum


class Day(Enum):
    MON = 0
    TUE = 1
    WED = 2
    THU = 3
    FRI = 4
    SAT = 5
    SUN = 6

    def difference(self, day):
        diff = day.value - self.value
        if diff > 3:
            return diff - 7
        elif diff < -3:
            return diff + 7
        else:
            return diff

    def readable(self):
        return {
            Day.MON: "Poniedziałek",
            Day.TUE: "Wtorek",
            Day.WED: "Środa",
            Day.THU: "Czwartek",
            Day.FRI: "Piątek",
            Day.SAT: "Sobota",
            Day.SUN: "Niedziela"
        }[self]

def nthDayFrom(n, day):
    return Day((day.value + n) % 7)

from typing import List
from term import Term
from lesson import Lesson
from action import Action


class BasicTimetable:

    def __init__(self):
        self.lesson_dict = {}

    def put(self, lesson: Lesson) -> bool:
        if type(lesson) is not Lesson:
            raise TypeError('Argument \'put()\' musi być typu \'Lesson\'')
        else:
            for les in list(self.lesson_dict.values()):
                if les.term == lesson.term:
                    raise ValueError(f'Podany termin jest zajęty')
            self.lesson_dict[f'{lesson.term.printStartTime()}-{lesson.term.printEndTime()}-{lesson.term.day}'] = lesson
            return True

    def parse(self, actions: List[str]) -> List[Action]:
        action_list = []
        for ac in actions:
            if ac in Action._value2member_map_:
                action_list.append(Action(ac))
            else:
                raise ValueError(f'Translacja {ac} jest niepoprawna')
        return action_list

    def perform(self, actions: List[Action]):
        lc = 0
        for ac in actions:
            if ac == Action.DAY_EARLIER:
                list(self.lesson_dict.values())[lc].earlierDay()
            elif ac == Action.DAY_LATER:
                list(self.lesson_dict.values())[lc].laterDay()
            elif ac == Action.TIME_EARLIER:
                list(self.lesson_dict.values())[lc].earlierTime()
            elif ac == Action.TIME_LATER:
                list(self.lesson_dict.values())[lc].laterTime()

            lc += 1
            lc %= len(list(self.lesson_dict.values()))

    def get(self, term: Term) -> Lesson:
        print("Wywołano metodę 'get()' zdefiniowaną w klasie 'BasicTimetable'")
        ltr = None
        for les in list(self.lesson_dict.values()):
            if les.term == term:
                ltr = les
                break
        return ltr

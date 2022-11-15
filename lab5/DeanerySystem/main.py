import sys
from day import Day
from term import Term
from Break import Break
from lesson import Lesson
from TimetableWithBreaks import Timetable2


term1 = Term(8, 0, Day.WED)
term2 = Term(9, 35, Day.WED)
term3 = Term(9, 40, Day.THU)

bl = [Break(Term(9, 30, Day.MON, 10)), Break(Term(11, 10, Day.MON, 10))]
tt2 = Timetable2(bl)


l1 = Lesson(tt2, term1, 'lesson1', 'lesson1', 2)
l1_new = Lesson(tt2, term1, 'lesson1_new', 'lesson1_new', 2)
l2 = Lesson(tt2, term2, 'lesson2', 'lesson2', 2)
l3 = Lesson(tt2, term3, 'lesson3', 'lesson3', 2)


print(tt2)

try:
    tt2.put(l1)
except Exception as e:
    print(e)
    sys.exit()

print(tt2)

try:
    tt2.put(l1_new)
except Exception as e:
    print(e)
    print()
    #sys.exit()

try:
    tt2.put(l2)
except Exception as e:
    print(e)
    print()
    #sys.exit()

# print(tt2)

try:
    tt2.put(l3)
except Exception as e:
    print(e)
    sys.exit()

print(tt2)

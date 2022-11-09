from day import Day
from term import Term
from lesson import Lesson
from timetable import Timetable1

term1 = Term(8, 0, Day.WED)
term2 = Term(12, 0, Day.WED)
term3 = Term(13, 30, Day.TUE)

tt1 = Timetable1()

P_Skryptowe = Lesson(tt1, term1, 'Skryptowe', 'Stanisław Polak', 2)
Kryptografia = Lesson(tt1, term2, 'Krypto', 'Paweł Topa', 2)
BLSK = Lesson(tt1, term3, 'BLSK', 'Jacek Rząsa', 2)

print(Kryptografia)
print()
#print(tt1)

tt1.put(P_Skryptowe)
tt1.put(Kryptografia)
tt1.put(BLSK)

print(tt1)

tt1.perform(tt1.parse(['d-', 't+', 't-', 'd+', 't+']))

print(tt1)

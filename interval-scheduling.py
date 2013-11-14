import time
from datetime import datetime

"""
Unweighted Interval scheduling algorithm.
Runtime complexity: O(n log n)
"""

class Interval(object):
    '''Date interval'''

    def __init__(self, title, start, finish):
        self.title = title
        self.start = int(time.mktime(datetime.strptime(start, "%d %b, %y").timetuple()))
        self.finish = int(time.mktime(datetime.strptime(finish, "%d %b, %y").timetuple()))

    def __repr__(self):
        return str((self.title, self.start, self.finish))



def schedule_unweighted_intervals(I):
    '''Use greedy algorithm to schedule unweighted intervals
       sorting is O(n log n), selecting is O(n)
       whole operation is dominated by O(n log n)
    '''

    I.sort(lambda x, y: x.finish - y.finish)  # f_1 <= f_2 <= .. <= f_n

    O = []
    finish = 0
    for i in I:
        if finish <= i.start:
            finish = i.finish
            O.append(i)

    return O

if __name__ == '__main__':
    I = []
    I.append(Interval("Summer School" , "14 Jan, 13", "24 Feb, 13"))
    I.append(Interval("Semester 1" , "1 Mar, 13", "4 Jun, 13"))
    I.append(Interval("Semester 2" , "18 Aug, 13", "24 Nov, 13"))
    I.append(Interval("Trimester 1" , "22 Mar, 13", "16 May, 13"))
    I.append(Interval("Trimester 2" , "22 May, 13", "24 Jul, 13"))
    I.append(Interval("Trimester 3" , "28 Aug, 13", "16 Nov, 13"))
    O = schedule_unweighted_intervals(I)


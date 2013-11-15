import bisect
import time
from datetime import datetime

"""
Weighted Interval scheduling algorithm.
Runtime complexity: O(n log n)
"""

class Interval(object):
    '''Date weighted interval'''

    def __init__(self, title, start, finish):
        self.title = title
        self.start = int(time.mktime(datetime.strptime(start, "%d %b, %y").timetuple()))
        self.finish = int(time.mktime(datetime.strptime(finish, "%d %b, %y").timetuple()))
        self.weight = self.finish - self.start

    def __repr__(self):
        return str((self.title, self.start, self.finish, self.weight))

def calculate_previous_intervals(I):
    '''For every interval j, calculate the rightmost mutually compatible interval i, where i < j
       I is a sorted list of Interval objects (sorted by finish time)
    '''
    # extract start and finish times
    start = [i.start for i in I]
    finish = [i.finish for i in I]

    p = []
    for j in xrange(len(I)):
        i = bisect.bisect_right(finish, start[j])  # rightmost interval f_i <= s_j
        if i:
            i -= 1  # ofset index
        p.append(i)

    return p


def schedule_weighted_intervals(I):
    '''Use dynamic algorithm to schedule weighted intervals
       sorting is O(n log n),
       finding p[1..n] is O(n log n),
       finding OPT[1..n] is O(n),
       selecting is O(n)
       whole operation is dominated by O(n log n)
    '''

    I.sort(lambda x, y: x.finish - y.finish)  # f_1 <= f_2 <= .. <= f_n
    p = calculate_previous_intervals(I)

    O = []
    finish = 0
    for i in I:
        print i

    return O

if __name__ == '__main__':
    I = []
    I.append(Interval("Summer School" , "14 Jan, 13", "24 Feb, 13"))
    I.append(Interval("Semester 1" , "1 Mar, 13", "4 Jun, 13"))
    I.append(Interval("Semester 2" , "18 Aug, 13", "24 Nov, 13"))
    I.append(Interval("Trimester 1" , "22 Mar, 13", "16 May, 13"))
    I.append(Interval("Trimester 2" , "22 May, 13", "24 Jul, 13"))
    I.append(Interval("Trimester 3" , "28 Aug, 13", "16 Nov, 13"))
    O = schedule_weighted_intervals(I)


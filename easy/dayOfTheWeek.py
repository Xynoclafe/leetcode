class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        noDays = 0
        curYear = 1971
        curMonth = 1
        while curYear < year:
            if curYear % 4 == 0 and (curYear % 100 != 0 or curYear % 400 == 0):
                noDays += 366
            else:
                noDays += 365
            curYear += 1
        while curMonth < month:
            if curMonth in [1, 3, 5, 7, 8, 10, 12]:
                noDays += 31
            elif curMonth in [4, 6, 9, 11]:
                noDays += 30
            elif curMonth == 2 and (year % 4 == 0 and (curYear % 100 != 0 or curYear % 400 == 0)):
                noDays += 29
            else:
                noDays += 28
            curMonth += 1
        noDays += day
        index = (noDays - 1) % 7
        return days[index]

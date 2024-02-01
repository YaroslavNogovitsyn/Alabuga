from datetime import datetime


def is_leap(year: int) -> bool:
    """Return True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


year1, month1, day1, hour1, min1, sec1 = map(int, input().split())
year2, month2, day2, hour2, min2, sec2 = map(int, input().split())

start = datetime(year1, month1, day1, hour1, min1, sec1)
end = datetime(year2, month2, day2, hour2, min2, sec2)

delta = end - start
days = delta.days
seconds = delta.seconds

print(days - sum(1 for curr_year in range(start.year, end.year + 1) if is_leap(curr_year)), seconds)

from calculate_age import get_age
import datetime
def test_get_age():
    # Given.
    yyyy, mm, dd = map(int, "1996/07/11".split("/"))   
    # When.
    age = get_age(yyyy, mm, dd)
    # Then.
    expected_age = datetime.date.today().year - 1996 - ((datetime.date.today().month, datetime.date.today().day) < (7, 11))
    assert age == expected_age

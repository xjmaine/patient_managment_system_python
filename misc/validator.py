import re
from datetime import datetime
from misc.constants import Constants


class DateValidator:
    # @staticmethod
    def validate_date_format(date_str):
        if not re.match(Constants.DATE_REGEX_PATTERN_MSG, date_str):
            raise ValueError(Constants.ERROR_INVALID_DATE_MSG)
        
        day, month, year = map(int, date_str.split('-'))
        
        if month < 1 or month > 12:
            raise ValueError(Constants.ERROR_INVALID_MONTH_MSG)
        
        if month == 2:
            if day > 29:
                raise ValueError(Constants.ERROR_FEB_MAX_DAYS_MSG)
            if day == 29:
                if not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
                    raise ValueError(Constants.ERROR_FEB_LEAP_YEAR_MSG)
        
        try:
            datetime.strptime(date_str, Constants.DATE_FORMAT_MSG)
        except ValueError:
            raise ValueError(Constants.ERROR_INVALID_DATE_FORMAT_MSG)
        
        return True
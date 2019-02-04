"""
36. Given str = "Today is 2012-11-27 and 2013/12/30 formats", return d/t format like
          str2 = "Today is 27-11-2012 and 30/12/2013 formats"
"""
import re
def change_format(text):
    text = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3-\2-\1', text)
    text = re.sub(r'(\d{4})/(\d{2})/(\d{2})', r'\3/\2-\1', text)
    return text












text = "Today is 2012-11-27 and 2013/12/30 formats"
print(change_format(text))
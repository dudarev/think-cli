CONTENT_TO_SORT = """
Some text
# Main title

## 2020-01-03 - Some other title
Some other text

## 2020-01-01 - Some title
Some text
## Some non-timestamp title
non-timestamp text
## 2020-01-02 - Some other title
Some other text
"""


SORTED_CONTENT_REVERSED = """Some text
# Main title


## Some non-timestamp title
non-timestamp text


## 2020-01-03 - Some other title
Some other text


## 2020-01-02 - Some other title
Some other text


## 2020-01-01 - Some title
Some text"""


SORTED_CONTENT = """Some text
# Main title


## Some non-timestamp title
non-timestamp text


## 2020-01-01 - Some title
Some text


## 2020-01-02 - Some other title
Some other text


## 2020-01-03 - Some other title
Some other text"""


CONTENT_TO_SORT_WITH_NON_TIMESTAMP = """## H2 heading

Some text

## 2020-01-03 - Some other title
Some other text

## 2020-01-01 - Some title
Some text
"""

CONTENT_WITH_NON_TIMESTAMP_SORTED = """## H2 heading

Some text


## 2020-01-01 - Some title
Some text


## 2020-01-03 - Some other title
Some other text"""


CONTENT_WITH_DATE_TO_SORT = """

## 2020-01-01 12:00 - Some title
Text
## 2020-01-03 12:00 - Some other title
Text
## 2019-01-01
Text
"""

CONTENT_WITH_DATE_SORTED_REVERSED = """## 2020-01-03 12:00 - Some other title
Text


## 2020-01-01 12:00 - Some title
Text


## 2019-01-01
Text"""

"""
Assets to test fanning out sections to files that are linked from the sections.
"""

# sections
SECTION_AT_NOON = """## 2020-01-01 12:00 - Some title at noon
Some text [[Non-existing link]]"""

SECTION_AT_MIDNIGHT = """## 2020-01-01 00:00 - Some title at midnight
Some text [[Existing link]] and dublicate [[Existing link]]
[[Non-existing link]]"""

SECTION_AT_SIX_AM_ALREADY_IN_EXISTING_LINK = """## 2020-01-01 06:00
Some text [[Existing link]]"""


# input
CONTENT_TO_FAN_OUT = f"""# Main title
Text

{SECTION_AT_SIX_AM_ALREADY_IN_EXISTING_LINK}


{SECTION_AT_NOON}


{SECTION_AT_MIDNIGHT}"""


# existing link
EXISTING_LINK_CONTENT_BEFORE = f"""# Existing link
Text


{SECTION_AT_SIX_AM_ALREADY_IN_EXISTING_LINK}"""


EXISTING_LINK_CONTENT_AFTER = f"""# Existing link
Text


{SECTION_AT_MIDNIGHT}


{SECTION_AT_SIX_AM_ALREADY_IN_EXISTING_LINK}"""


# link to create (non-existing)
NON_EXISTING_LINK_CONTENT_AFTER = f"""{SECTION_AT_MIDNIGHT}


{SECTION_AT_NOON}"""


# files
FILE_NAME_TO_FAN = "2020-01-01.md"
EXISTING_FILE_NAME = "Existing link.md"
NON_EXISTING_FILE_NAME = "Non-existing link.md"

FILES_IN = {
    FILE_NAME_TO_FAN: CONTENT_TO_FAN_OUT,
    EXISTING_FILE_NAME: EXISTING_LINK_CONTENT_BEFORE,
}


FILES_OUT = {
    FILE_NAME_TO_FAN: CONTENT_TO_FAN_OUT,
    EXISTING_FILE_NAME: EXISTING_LINK_CONTENT_AFTER,
    NON_EXISTING_FILE_NAME: NON_EXISTING_LINK_CONTENT_AFTER,
}

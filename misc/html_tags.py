def __html_tag_creator(text: str, tag: str) -> str:
    return f'<{tag}>{text}</{tag}>'


# region Tags

def b(text: str) -> str:
    return __html_tag_creator(text, 'b')


def i(text: str) -> str:
    return __html_tag_creator(text, 'i')

# endregion

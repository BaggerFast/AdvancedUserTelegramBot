def __html_tag_creator(text: str, tag: str) -> str:
    return f'<{tag}>{text}</{tag}>'


# region Tags

def b(text: str) -> str:
    return __html_tag_creator(text, 'b')


def i(text: str) -> str:
    return __html_tag_creator(text, 'i')


def url(text: str, hyper_url: str):
    return f'<a href="{hyper_url}">{text}</a>'

# endregion

from django.template.defaulttags import register


@register.filter
def youtube_url(val: str):
    if "https://www.youtube.com/" in val or "https://youtu.be/" in val:

        if 'embed' not in val:
            url_end = val.split('/')[-1]

            val = f'https://www.youtube.com/embed/{url_end}'

        return val
from django.template.defaulttags import register


@register.simple_tag(takes_context=True)
def field_data(context, **kwargs):
    request_post = context.get("request_post")
    object = context.get('object') if kwargs.get("object") == None else kwargs.get("object")
    lang = kwargs.get('lang')
    field = kwargs.get("field")

    if request_post:
        data_dict = request_post
    elif object:
        data_dict = object.__dict__
    else:
        return ''
    

    field_data = data_dict.get(field, {})

    if type(field_data) != dict:
        if field_data is None:
            return ''

        return field_data

    data = field_data.get(lang.code, '')
    
    return data

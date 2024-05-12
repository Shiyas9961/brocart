from django import template

register = template.Library()

@register.filter(name = 'chunks')
def chunks (prod_list, chunk_size) :

    chunk_arr = []
    i = 0
    for prod in prod_list :
        chunk_arr.append(prod)
        i += 1
        if i == chunk_size :
            yield chunk_arr
            i = 0
            chunk_arr = []
    if chunk_arr:
        yield chunk_arr
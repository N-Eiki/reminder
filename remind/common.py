from django import template

register = template.Library()


class SetVarNode(template.Node):

    def __init__(self, var_name, var_value):
        self.var_name = var_name
        self.var_value = var_value

    def render(self, context):
        try:
            value = template.Variable(self.var_value).resolve(context)
        except template.VariableDoesNotExist:
            value = ""
        context[self.var_name] = value

        return u""


@register.tag(name='set')
def set_var(parser, token):
    """
    {% set some_var = '123' %}
    """
    parts = token.split_contents()
    if len(parts) < 4:
        raise template.TemplateSyntaxError("'set' tag must be of the form: {% set <var_name> = <var_value> %}")

    return SetVarNode(parts[1], parts[3])

@register.filter
def make_list(ele1, ele2):
    return [ele1, ele2]

@register.filter
def display(state, alldata):
    res = ""

    for data in alldata:
        if data[1]==state[0] and data[2]==state[1]:
            res=data[0]
            break;
        else:
            res="予定なし"
    return res

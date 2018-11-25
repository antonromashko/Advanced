import re


def multiple_parser(parser_func):
    def wrapped(host):
        return list(map(parser_func, host))
    return wrapped


@multiple_parser
def host_parser(host):
    parse = re.search(r'^((?:(?:(?:\d|[1-9]\d|1\d{2}|2[0-5]{2}|2[0-4]\d)\.){3}'
                      r'(?:\d|[1-9]\d|1\d{2}|2[0-5][0-4]|2[0-4]\d))'
                      r'|(?:[a-zA-Z]+(?:\.[a-zA-Z]*)*)):(\d+)$', host)
    try:
        return parse.groups()
    except AttributeError:
        return parse


my_host = ['1.0.0.254:5000', 'tap.com:9000', '12.44.33.0254:9000']
my_host_parse = host_parser(my_host)
print(my_host_parse)
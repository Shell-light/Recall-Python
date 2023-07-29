msg_template= """Hello {name},
Thank you  for joing {website}. We are very happy to have
you with us.
"""#.format(name="Light", website="Shell-light")

def format_msg(my_name="Light", my_website="Ashell"):
    my_msg = msg_template.format(name=my_name, website=my_website)
    print(my_msg)
    return my_msg


def base_fanction(*args, **kwagrs):
    print(args, kwagrs)
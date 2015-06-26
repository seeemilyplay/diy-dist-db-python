import node

def write(node_urls, thing):
    #todo: only works with one node, need to make distributed!
    node.put_thing(node_urls[0], thing)

def read(node_urls, id):
    #todo: only works with one node, need to make distributed!
    return node.get_thing(node_urls[0], id)


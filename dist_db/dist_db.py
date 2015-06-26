import node

def try_to_write(node_url, thing):
    try:
        node.put_thing(node_url, thing)
        return True
    except:
        return False

def write(node_urls,
          replication_factor,
          write_consistency,
          thing):
    results = [ try_to_write(u, thing) for u in node_urls[:replication_factor] ]
    success_count = sum(results)
    if success_count < write_consistency:
       raise Exception('Only wrote to {0} nodes'.format(success_count))

def read(node_urls, id):
    #todo: only works with one node, need to make distributed!
    return node.get_thing(node_urls[0], id)


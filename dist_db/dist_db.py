import node
from operator import attrgetter

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

def read(node_urls,
         replication_factor,
         read_consistency,
         id):
    things = []
    for u in node_urls[:replication_factor]:
        if len(things) < read_consistency:
            try:
                things.append(node.get_thing(u, id))
            except:
                pass
    if len(things) < read_consistency:
        raise Exception('Only read from {0} nodes'.format(len(things)))
    return max(things, key=attrgetter('timestamp'))

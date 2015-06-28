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

def resolve(things):
    non_nones = [ t for t in things if t is not None ]
    return max(non_nones, key=attrgetter('timestamp'))

def read_repair(node_urls,
                replication_factor,
                id):
    things = [] 
    for u in node_urls[:replication_factor]:
        try:
            things.append(node.get_thing(u, id))
        except:
            things.append(None) 
    thing = resolve(things)
    for idx, t in enumerate(things):
        # see if it's broken, and if it is fix it
        if t is None or t.value != thing.value:
            node.put_thing(node_urls[idx], thing)    

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
    read_repair(node_urls, replication_factor, id)
    return resolve(things)

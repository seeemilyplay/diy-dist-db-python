import dist_db
from thing import Thing

node_urls = ['http://localhost:8080']
dist_db.write(node_urls, Thing(3, 'foo'))
dist_db.write(node_urls, Thing(7, 'bar'))
thing_3 = dist_db.read(node_urls, 3)
thing_7 = dist_db.read(node_urls, 7)
print thing_3
print thing_7

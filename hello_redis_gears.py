from gearsclient import GearsRemoteBuilder as GRB
from gearsclient import execute
import redis

conn = redis.Redis('localhost',6379)
grb = GRB(reader='KeysReader', r=conn)
grb.filter(lambda  x: x['key']=='test')
#print(grb.run(mode='async'))


grb = GRB(reader='KeysOnlyReader', r=conn)
grb.filter(lambda  x: x=='test')
grb.map(lambda x: execute('incrby','count',1))
#print(grb.run(mode='async'))

#BC

grb = GRB(reader='KeysReader', r=conn)
grb.filter(lambda  x: x['key'].startswith('raza:logs:model1:'))
print(grb.run(mode='async'))

#coding:utf-8

# 集合覆盖问题

states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
# 广播清单
stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['id', 'wa', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

final_station = []

while states_needed:
    best_station = None
    best_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(best_covered):
            best_station = station
            best_covered = covered
    
    states_needed -= best_covered
    # stations.pop(best_station)
    final_station.append(best_station)

print(final_station)

import ciw

N = ciw.create_network(
     arrival_distributions=[ciw.dists.Exponential(0.2)],
     service_distributions=[ciw.dists.Exponential(0.1)],
     number_of_servers=[3]
 )

# --------- Test 10 fois de la simulation -----------#

toutes_moyenne_waiting_time = []
toutes_moyenne_service_time  = []
toutes_moyenne_time_in_sys = []
toutes_pourcentage_activité_serveurs =[]

for trail in range(10):
    ciw.seed(trail)
    Q = ciw.Simulation(N)
    Q.simulate_until_max_time(480)
    data = Q.get_all_records()

    serviceTimes = [r.service_time for r in data]
    waitingTimes = [r.waiting_time for r in data]
    time_in_sys = [(r.service_time + r.waiting_time) for r in data]

    moyenne_service_time = sum(serviceTimes) / len(serviceTimes)
    moyenne_waiting_time = sum(waitingTimes) / len(waitingTimes)
    moyenne_time_in_sys = sum(time_in_sys) / len(time_in_sys)
    pourcentage_activité_serveurs = Q.transitive_nodes[0].server_utilisation

    toutes_moyenne_waiting_time.append(moyenne_waiting_time)
    toutes_moyenne_service_time.append(moyenne_service_time)
    toutes_moyenne_time_in_sys.append(moyenne_time_in_sys)
    toutes_pourcentage_activité_serveurs.append(pourcentage_activité_serveurs)

avg_time_in_sys = sum(toutes_moyenne_time_in_sys)/10
avg_waiting_time = sum(toutes_moyenne_waiting_time)/10
avg_service_time = sum(toutes_moyenne_service_time)/10
avg_pourcentage_occup = sum(toutes_pourcentage_activité_serveurs)/10

print("avg_time_in_sys = ",avg_time_in_sys)
print("avg_waiting_time = ", avg_waiting_time)
print("avg_service_time = ", avg_service_time )
print("avg_pourcentage_occup = ", avg_pourcentage_occup, "%" )


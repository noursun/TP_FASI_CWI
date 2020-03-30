import ciw

#---- Comparaison entre l'étude théorique et les résultats de la simulation dans un sys M/M/1 -----#
# 1. Etude théorique :

taux_arrive = 5
taux_service = 10
#  R < 1

moyenne_Ts = 1 / (taux_service - taux_arrive)
moyenne_Tf = taux_arrive / (taux_service*(taux_service - taux_arrive))

print("Résultats de l'étude théorique :")
print("moyenne_time_in_sys = ",moyenne_Ts)
print("moyenne_waiting_time = ", moyenne_Tf )

# 2. La simulation :

N=ciw.create_network (
    arrival_distributions=[ciw.dists.Exponential(5)],
    service_distributions=[ciw.dists.Exponential(10)],
	number_of_servers=[1]
	)

toutes_moyenne_waiting_time = []
toutes_moyenne_time_in_sys = []

for trail in range(10):
    ciw.seed(trail)
    Q = ciw.Simulation(N)
    Q.simulate_until_max_time(1000)
    data = Q.get_all_records()

    waitingTimes = [r.waiting_time for r in data]
    time_in_sys = [(r.service_time + r.waiting_time) for r in data]

    moyenne_waiting_time = sum(waitingTimes) / len(waitingTimes)
    moyenne_time_in_sys = sum(time_in_sys) / len(time_in_sys)

    toutes_moyenne_waiting_time.append(moyenne_waiting_time)
    toutes_moyenne_time_in_sys.append(moyenne_time_in_sys)

avg_time_in_sys = sum(toutes_moyenne_time_in_sys)/10
avg_waiting_time = sum(toutes_moyenne_waiting_time)/10

print("Résultats de la simulation :")
print("moyenne_time_in_sys = ",avg_time_in_sys)
print("moyenne_waiting_time = ", avg_waiting_time )

print("l'Erreur :")
print("erreur_moyenne_time_in_sys = ",avg_time_in_sys - moyenne_Ts)
print("erreur_moyenne_waiting_time = ", avg_waiting_time - moyenne_Tf )
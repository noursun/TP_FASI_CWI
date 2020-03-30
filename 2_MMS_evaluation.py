import matplotlib.pyplot as plt
import ciw

# ------------- Définition du systeme d'attente M/M/3 ------------------ #
N = ciw.create_network(
     arrival_distributions=[ciw.dists.Exponential(0.2)],
     service_distributions=[ciw.dists.Exponential(0.1)],
     number_of_servers=[3]
 )

# ------------ Définition d'un seed ------------------#
ciw.seed(1)

# --------------- Création de la Simulation --------------#
Q = ciw.Simulation(N)

# --------------- La durée simulée ----------------------#
Q.simulate_until_max_time (480,progress_bar=True)

#----------- les données de tous les individus qui ont terminé le service --------#
data = Q.get_all_records()

# ----------------------- des infos ------------------------#
serviceTimes = [r.service_time for r in data]
waitingTimes = [r.waiting_time for r in data]
time_in_sys = [(r.service_time + r.waiting_time) for r in data]

print("\nService times ***********************")
print(serviceTimes)
print("\nWaiting times ***********************")
print(waitingTimes)

# ----------------------- caractéristiques du système ------------------------#
moyenne_service_time = sum(serviceTimes)/len(serviceTimes)
moyenne_waiting_time = sum(waitingTimes)/len(waitingTimes)
moyenne_time_in_sys = sum(time_in_sys)/len(time_in_sys)
pourcentage_activité_serveurs = Q.transitive_nodes[0].server_utilisation

print("\nTemps moyen dans le système ***********************")
print("moyenne_time_in_sys = ",moyenne_time_in_sys)
print("\nTemps moyen dans la file ***********************")
print("moyenne_waiting_time = ", moyenne_waiting_time )
print("\nTemps moyen dans le service ***********************")
print("moyenne_service_time = ", moyenne_service_time )
print("\n% d'utilisation des serveurs ***********************")
print("pourcentage_activité_serveurs = ", pourcentage_activité_serveurs, "%" )

# ------------------------ Graphe ----------------------------- #
plt.hist(waitingTimes)
plt.show()



import ciw

# ------------- Définition du systeme d'attente M/M/3 ------------------ #
# time unit = min
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

# ------- la liste des individus qui ont fini leurs services à la fin de simulation  ------- #
print("\n-----------------------------------------------------------------\n")
print("la liste des individus qui ont fini leurs services à la fin de simulation :\n")

print(Q.nodes[-1].all_individuals)

# ------ infos du premier individus à avoir terminé le service ------ #
print("\n-----------------------------------------------------------------\n")
print("infos du premier individus à avoir terminé le service : \n")
ind = Q.nodes[-1].all_individuals[0]

print(ind)
print(ind.data_records)

# ------ infos de tous les individus qui ont terminé leurs services ------ #
print("\n-----------------------------------------------------------------\n")
print("infos de tous les individus qui ont terminé leurs services : \n")
for ind in Q.nodes[-1].all_individuals :
    print(ind)
    print(ind.data_records)
    print("\n******************************")

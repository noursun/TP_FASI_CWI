import ciw
import matplotlib.pyplot as plt

def probability_of_baulking(n):
    if n<3:
        return 0.0
    if n<7:
        return 0.5
    return 1.0

N=ciw.create_network (
    arrival_distributions=[ciw.dists.Exponential(5)],
    service_distributions=[ciw.dists.Exponential(10)],
	baulking_functions=[probability_of_baulking],
	number_of_servers=[1]
	)

ciw.seed(1)
Q=ciw.Simulation(N)
Q.simulate_until_max_time (200,progress_bar=True)

print ("le nombre de client refusés durant 200 unités de temps est: ", len(Q.baulked_dict[1][0]))
print ("La liste des dates ou des client ont été refusés")
print (Q.baulked_dict)

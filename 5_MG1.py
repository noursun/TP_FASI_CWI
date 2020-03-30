import ciw

N=ciw.create_network (
	arrival_distributions=[ciw.dists.Exponential(0.1)],
	service_distributions=[ciw.dists.Pmf([20,1],[0.2,0.8])],
	number_of_servers=[1]
	)
ciw.seed(1)
Q=ciw.Simulation(N)
Q.simulate_until_max_time (20000,progress_bar=True)
data=Q.get_all_records()

service_times=[client.service_time for client in data ]
moyenne_service_times=sum(service_times)/ len(service_times)
print ("La durée moyenne de service est: ",moyenne_service_times)

waiting_times=[client.waiting_time for client in data ]
moyenne_waiting_times=sum(waiting_times)/ len(waiting_times)
print ("La durée moyenne d'attente est: ",moyenne_waiting_times)

system_times=[client.service_end_date-client.arrival_date for client in data ]
moyenne_system_times=sum(system_times)/ len(system_times)
print ("La durée moyenne dans le système est: ",moyenne_system_times)

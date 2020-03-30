import ciw

# time unit = h
N=ciw.create_network (
	arrival_distributions=[ciw.dists.Exponential(60)],
	service_distributions=[ciw.dists.Exponential(20)],
	number_of_servers=[4],
	queue_capacities=[4]
	)

ciw.seed(1)
Q=ciw.Simulation(N)
Q.simulate_until_max_time (8,progress_bar=True)
data=Q.get_all_records()

service_times=[client.service_time for client in data ]
moyenne_service_times=sum(service_times)/ len(service_times)
print ("La durée moyenne de service est: ", moyenne_service_times)

waiting_times=[client.waiting_time for client in data ]
moyenne_waiting_times=sum(waiting_times)/ len(waiting_times)
print ("La durée moyenne d'attente est: ", moyenne_waiting_times)

times_in_sys=[client.service_end_date-client.arrival_date for client in data ]
moyenne_times_in_sys=sum(times_in_sys)/ len(times_in_sys)
print ("La durée moyenne dans le système est: ",moyenne_times_in_sys)
print ("le nombre de clients durant les 8h est:  ",len(Q.get_all_records()))
print ("Le nombre de clients rejetés pendant les 8h est:  ",len(Q.rejection_dict[1][0]))
print ("le pourcentage de rejet est: ", round(len(Q.rejection_dict[1][0])/len(Q.get_all_records())
                                              *100,2), "%")
print ("La liste des dates ou des clients ont été rejetés:")
print (Q.rejection_dict[1][0])















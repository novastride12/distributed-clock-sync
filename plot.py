import matplotlib.pyplot as plt

clients = [5, 10, 20, 50]
delays = [0.002, 0.003, 0.005, 0.009]   # put your values here

plt.plot(clients, delays, marker='o')
plt.xlabel("Number of Clients")
plt.ylabel("Average Delay")
plt.title("Scalability Test")
plt.grid()

plt.show()
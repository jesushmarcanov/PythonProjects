import speedtest

servers = []
# If you want to test against a specific server
# servers = [1234]

s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download()
s.upload()
s.results.share()

results_dict = s.results.dict()
print(f"Download speed: {results_dict['download'] / 10**6:.2f} Mbps")
print(f"Upload speed: {results_dict['upload'] / 10**6:.2f} Mbps")
print(f"Ping: {results_dict['ping']:.2f} ms")
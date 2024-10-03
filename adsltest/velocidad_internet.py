import speedtest

st = speedtest.Speedtest()
downLoadSpeed = st.download()
upLoadSpeed = st.upload()
ping = st.results.ping
print(f"Download Speed: {downLoadSpeed} Mbps")
print(f"Upload Speed: {upLoadSpeed} Mbps")
print(f"Ping: {ping} ms")
import speedtest

speed = speedtest.Speedtest()
print(f"Downloading speed : { speed.download() } ")
print(f"Uploading speed : { speed.upload() } ")
import pyaudio

"""
デバイスうえでのオーディオ系の機器情報を表示する
"""
pa = pyaudio.PyAudio()

for i in range(pa.get_device_count()):
    print(pa.get_device_info_by_index(i))
    print()

pa.terminate()
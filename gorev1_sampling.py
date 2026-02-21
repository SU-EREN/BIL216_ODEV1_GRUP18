import numpy as np
import matplotlib.pyplot as plt


f_signal = 5  

# Süre (saniye)
duration = 1  

# Sürekli zaman (yüksek çözünürlük)
t_cont = np.linspace(0, duration, 1000)
signal_cont = np.sin(2 * np.pi * f_signal * t_cont)

# Örnekleme frekansları
sampling_rates = [8, 20, 50]

plt.figure(figsize=(10, 6))

# Sürekli sinyali çiz
plt.plot(t_cont, signal_cont, label="Orijinal Sinyal", linewidth=2)

# Farklı örnekleme frekansları için noktaları çiz
for fs in sampling_rates:
    t_sampled = np.linspace(0, duration, fs)
    signal_sampled = np.sin(2 * np.pi * f_signal * t_sampled)
    plt.scatter(t_sampled, signal_sampled, label=f"Fs = {fs} Hz")

plt.title("Sampling Ornegi")
plt.xlabel("Zaman (s)")
plt.ylabel("Genlik")
plt.legend()
plt.grid(True)
plt.show()

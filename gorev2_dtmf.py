import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import tkinter as tk

# Örnekleme parametreleri
fs = 8000
T = 0.3
t = np.linspace(0, T, int(fs*T), endpoint=False)

# DTMF frekans tablosu
dtmf_freq = {
    '1': (697, 1209),
    '2': (697, 1336),
    '3': (697, 1477),
    'A': (697, 1633),
    '4': (770, 1209),
    '5': (770, 1336),
    '6': (770, 1477),
    'B': (770, 1633),
    '7': (852, 1209),
    '8': (852, 1336),
    '9': (852, 1477),
    'C': (852, 1633),
    '*': (941, 1209),
    '0': (941, 1336),
    '#': (941, 1477),
    'D': (941, 1633),
}

def play_tone(key):
    f1, f2 = dtmf_freq[key]
    signal = (np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t)) / 2
    sd.play(signal, fs)
    
    # --- FFT HESABI (KASTETTİĞİM GRAFİK BURASI) ---
    n = len(signal)
    freqs = np.fft.rfftfreq(n, d=1/fs)
    spectrum = np.abs(np.fft.rfft(signal))

    plt.figure(figsize=(10, 4))
    
    # 1. Zaman Domaini (Şu an raporda olan)
    plt.subplot(1, 2, 1)
    plt.plot(t[:200], signal[:200]) 
    plt.title(f"{key} Tuşu - Zaman Domaini")
    plt.grid(True)

    # 2. Frekans Domaini (Rapora eklemen gereken FFT)
    plt.subplot(1, 2, 2)
    plt.plot(freqs, spectrum)
    plt.xlim(500, 2000) # Tuşların frekans aralığına zoom yapar
    plt.title(f"{key} Tuşu - FFT (Spektrum)")
    plt.xlabel("Frekans (Hz)")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# GUI oluşturma
root = tk.Tk()
root.title("DTMF Sinyal Üretici")

keys = [
    ['1','2','3','A'],
    ['4','5','6','B'],
    ['7','8','9','C'],
    ['*','0','#','D']
]

for r, row in enumerate(keys):
    for c, key in enumerate(row):
        button = tk.Button(root, text=key, width=5, height=2,
                           command=lambda k=key: play_tone(k))
        button.grid(row=r, column=c)

root.mainloop()


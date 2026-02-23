 BIL216_ODEV1_GRUP18

Sinüzoidal İşaretler ve DTMF Sinyal Sentezi

Bu çalışmada sinüzoidal işaretlerin örneklenmesi ve Nyquist örnekleme teoremi incelenmiş, ayrıca DTMF (Dual Tone Multi Frequency) sistemi yazılım ortamında modellenmiştir.

 1. Sinüzoidal İşaret ve Örnekleme Analizi

Bu bölümde 5 Hz frekanslı bir sinüzoidal sinyal üretilmiştir.  
Sinyal farklı örnekleme frekansları (8 Hz, 20 Hz, 50 Hz) ile örneklenerek grafiksel olarak karşılaştırılmıştır.

Amaç:

- Örnekleme frekansının sinyal temsilindeki etkisini gözlemlemek
- Nyquist kriterini görsel olarak doğrulamak

Nyquist teoremine göre:

fs ≥ 2fmax

Bu koşul sağlanmadığında aliasing oluşabileceği gösterilmiştir.

2. DTMF Sinyal Sentezi

DTMF sistemi, her tuş için iki farklı frekansın toplamından oluşan bir sinyal üretir:

x(t) = sin(2πf₁t) + sin(2πf₂t)

Projede:

- Örnekleme frekansı (fs): 8000 Hz
- Sinyal süresi (T): 0.3 saniye
- Genlik normalizasyonu uygulanmıştır.

En yüksek DTMF frekansı 1633 Hz olduğundan:

2 × 1633 = 3266 Hz

Seçilen 8000 Hz örnekleme frekansı Nyquist kriterini sağlamaktadır.

 3. FFT Analizi

Her tuş için:

- Zaman domeni grafiği
- Frekans domeni (FFT) grafiği

oluşturulmuştur.

Spektrum analizinde ilgili tuşa ait iki frekans bileşeninin keskin tepe noktaları olarak gözlemlenmesi, sentezin doğruluğunu göstermektedir.

4. Kullanılan Kütüphaneler

- NumPy
- Matplotlib
- SoundDevice
- Tkinter

5. Sonuç

Nyquist kriterine uygun örnekleme frekansı seçildiğinde sinyaller doğru şekilde temsil edilmiştir.  
DTMF sistemi başarıyla sentezlenmiş ve FFT analizi ile frekans doğrulaması yapılmıştır.

Turing Makinesi ile Plaka Tanıma
Türk araç plakalarının NNLLNNN biçimine (2 rakam, 2 harf, 3 rakam) uyup uymadığını kontrol eden bir Turing makinesi simülasyonu. Python ile yazıldı.

Örnek: 55AB123 → KABUL, 5AB123 → RED

Nasıl çalışır?

Makine bant üzerinde soldan sağa ilerler ve her karakterde bir durum geçiş tablosuna bakar:

q0 → q1 → q2: iki rakam bekler
q2 → q3 → q4: iki büyük harf bekler
q4 → q5 → q6 → q7: üç rakam bekler
q7: bandın sonuna (_) gelindiyse kabul
Beklenmeyen bir karakter okunduğu anda makine red durumuna geçer. Her adımda mevcut durum, okunan sembol ve kafa hareketi ekrana yazdırılır.

Tam geçiş tablosu ve durum diyagramı için: gecis_tablosu.md

Çalıştırma

Etkileşimli mod (çıkmak için q):

python turing_machine.py

Hazır test girdileriyle:

python turing_machine.py --test

**Not**

Bu proje yalnızca NNLLNNN biçimini tanır. Gerçek Türk plakalarında harf sayısı 1–3, son rakam grubu 2–4 hane olabilir (ör. 34A1234). Bu biçimler şu an reddedilir.

# 🚗 Turing Makinesi ile Plaka Tanıma

Türk araç plakalarının `NNLLNNN` formatına (2 rakam, 2 harf, 3 rakam) uyup uymadığını karakter karakter kontrol eden bir Turing makinesi simülasyonu.

> `55AB123` → ✅ KABUL
>
> `5AB123` → ❌ RED

## 🎯 Özellikler

- ✅ Durum geçiş tablosuna dayalı plaka doğrulama
- ✅ Her adımda durum, okunan sembol ve kafa hareketinin gösterilmesi
- ✅ Etkileşimli mod: istediğin plakayı yazıp anında sonucu gör
- ✅ Hazır test senaryoları (`--test`): geçerli ve geçersiz 11 farklı girdi
- ✅ Geçiş tablosu ve Mermaid durum diyagramı ile dokümantasyon

## 🛠️ Teknik Detaylar

- **Geçiş Fonksiyonu:** `δ(durum, sembol) → yeni_durum` kuralları bir sözlükte (dictionary) tutulur. Makine her adımda tabloya bakar; tabloda karşılığı olmayan her geçiş doğrudan `q_reject` durumuna gider.
- **8 Durumlu Yapı:** `q0`'dan `q7`'ye kadar her durum, plakadaki bir karakter pozisyonunu temsil eder (tablo aşağıda).
- **Uzunluk Kontrolü:** Bandın sonuna boşluk (`_`) sembolü eklenir. Makine 7 karakteri okuduktan sonra boşluk görmezse plakayı fazla uzun sayar ve reddeder.
- **Büyük/Küçük Harf Duyarlılığı:** Yalnızca büyük harfler (`A-Z`) kabul edilir; `55ab123` reddedilir.

| Durumlar | Beklenen |
|---|---|
| `q0 → q1 → q2` | 2 rakam (il kodu) |
| `q2 → q3 → q4` | 2 büyük harf |
| `q4 → q5 → q6 → q7` | 3 rakam |
| `q7 → q_accept` | Bant sonu (`_`) |

📄 Tam geçiş tablosu ve durum diyagramı: [gecis_tablosu.md](gecis_tablosu.md)

## 🚀 Çalıştırma

Etkileşimli mod (çıkmak için `q`):

```bash
python turing_machine.py
```

Test senaryoları:

```bash
python turing_machine.py --test
```

## 📸 Örnek Çıktı

```
Lütfen kontrol edilecek plakayı girin: 55AB123
--- Simülasyon Başlıyor ---
Başlangıç Bandı: 55AB123_
Durum: q0, Okunan: '5', Yeni Durum: q1, Kafa Hareketi: R, Bant: 55AB123_
Durum: q1, Okunan: '5', Yeni Durum: q2, Kafa Hareketi: R, Bant: 55AB123_
Durum: q2, Okunan: 'A', Yeni Durum: q3, Kafa Hareketi: R, Bant: 55AB123_
...
Durum: q7, Okunan: '_', Yeni Durum: q_accept, Kafa Hareketi: -, Bant: 55AB123_
------------------------------
Sonuç: KABUL
```

## 💡 Geliştirilebilir

Gerçek Türk plakalarında harf sayısı 1–3, son rakam grubu 2–4 hane olabilir (ör. `34A1234`, `06ABC12`). Makine şu an yalnızca `NNLLNNN` formatını tanıyor; durum sayısı artırılarak tüm formatlar desteklenebilir.

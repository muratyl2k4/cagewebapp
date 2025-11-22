# Django Beslenme ve Diyet Uygulaması

Bu proje, kullanıcıların beslenme bilgilerini girerek kişiselleştirilmiş diyet ve pre-workout programı oluşturmasını sağlayan bir Django web uygulamasıdır. Uygulama, kullanıcıların hedeflerine göre günlük kalori ve makro besin dağılımlarını hesaplar ve her öğün için önerilen besinleri listeler.

---

## Kullanıcıdan Alınan Veriler

1. **Temel Bilgiler**

   * Kilo (kg)
   * Boy (cm)
   * Yaş (yıl)
   * Cinsiyet (Kadın / Erkek)
   * Günlük Aktivite Seviyesi (Az / Orta / Çok / Aşırı)
   * Hedef Kilo (Kilo alma (KG+) / Kilo verme (KG-))
   * Hedef Kilo Aralığı (kg)

2. **Öğün Bilgileri**

   * Günlük Öğün Sayısı (1-8)
   * Her Öğün için Seçilen Besinler: Protein ve Karbonhidrat

3. **Pre-Workout ve Takviyeler**

   * Muz, Hurma, Kahve, Pre-Workout, Churcill, BCAA

---

## Matematiksel Hesaplamalar

### 1. Bazal Metabolizma Hızı (BMR)

* **Kadınlar için:**

```
BMR = 655 + (4.35 × kilo (lbs)) + (4.7 × boy (inç)) - (4.7 × yaş)
```

* **Erkekler için:**

```
BMR = 66 + (6.23 × kilo (lbs)) + (12.7 × boy (inç)) - (6.76 × yaş)
```

> Kilogramdan pound ve santimetreden inçe dönüşüm yapılır.

### 2. Aktivite Seviyesi ile Günlük Kalori (TDEE)

| Aktivite Seviyesi | Çarpan |
| ----------------- | ------ |
| Az                | 1.2    |
| Orta              | 1.375  |
| Çok               | 1.55   |
| Aşırı             | 1.725  |

```
TDEE = BMR × Aktivite Çarpanı
```

### 3. Hedef Kilo ile Günlük Kalori Ayarlaması

* 1 kg yağ ≈ 7777 - 8000 kcal
* Kilo alma (KG+):

```
Günlük Kalori = TDEE + (Hedef Kilo × 7777 ÷ 30)
```

* Kilo verme (KG-):

```
Günlük Kalori = TDEE - (Hedef Kilo × 8000 ÷ 30)
```

### 4. Makro Dağılımı

* Protein: Kilo × 2 g
* Yağ: Kilo × 0.65 g
* Karbonhidrat: Kalan kalorilerden hesaplanır

```
Karb (g) = (Günlük Kalori - (Protein g × 4 + Yağ g × 9)) ÷ 4
```

### 5. Öğün Başına Dağılım

```
Öğün Protein = Günlük Protein ÷ Öğün Sayısı
Öğün Karb = Günlük Karbonhidrat ÷ Öğün Sayısı
Öğün Yağ = Günlük Yağ ÷ Öğün Sayısı
```

---

## Örnek Hesaplama

**Kullanıcı Bilgileri:**

| Parametre          | Değer            |
| ------------------ | ---------------- |
| Kilo (kg)          | 70               |
| Boy (cm)           | 175              |
| Yaş (yıl)          | 25               |
| Cinsiyet           | Erkek            |
| Aktivite Seviyesi  | Orta             |
| Hedef Kilo         | Kilo Alma (2 kg) |
| Günlük Öğün Sayısı | 4                |

### BMR Hesaplama

* Kilo: 70 kg → 154.32 lbs
* Boy: 175 cm → 68.9 inç

```
BMR = 66 + (6.23 × 154.32) + (12.7 × 68.9) - (6.76 × 25) ≈ 1733 kcal/gün
```

### Günlük Kalori (TDEE)

```
TDEE = BMR × 1.375 ≈ 2383 kcal/gün
```

### Hedef Kilo Kalorisi

```
Günlük Kalori = 2383 + (2 × 7777 ÷ 30) ≈ 2901 kcal/gün
```

### Makro Dağılımı

```
Protein = 70 × 2 = 140 g
Yağ = 70 × 0.65 ≈ 45.5 g
Karb = (2901 - (140×4 + 45.5×9)) ÷ 4 ≈ 483 g
```

### Öğün Başına Makro

```
Öğün Protein = 35 g
Öğün Yağ ≈ 11.4 g
Öğün Karb ≈ 120.75 g
```

### Öğün Tablosu

| Öğün | Protein (g) | Karbonhidrat (g) | Yağ (g) |
| ---- | ----------- | ---------------- | ------- |
| 1    | 35          | 121              | 11      |
| 2    | 35          | 121              | 11      |
| 3    | 35          | 121              | 11      |
| 4    | 35          | 120              | 12      |

### Pre-Workout Önerisi

* Kahve: 70 kg × 4 mg = 280 mg max
* Diğer takviyeler: Muz, Hurma, BCAA, Pre-Workout, Churcill (kullanıcı seçimine göre)

---

## Sistem İşleyişi

1. Kullanıcı temel bilgilerini girer.
2. Sistem BMR ve günlük kalori ihtiyacını hesaplar.
3. Kullanıcı hedefini seçer ve günlük kalori ayarlanır.
4. Öğün sayısı girilir ve her öğün için protein, karbonhidrat ve yağ miktarı belirlenir.
5. Pre-workout ve takviyeler kullanıcıya uygun şekilde önerilir.
6. Kullanıcı öğün bazlı besin seçimlerini yapar.
7. `diet` sayfası tüm öğünleri, besinleri ve gramajları gösterir.

---

## Kullanılan Besinler

**Protein:** Tavuk Göğsü, Balık, Hindi
**Karbonhidrat:** Pirinç, Bulgur, Yulaf, Makarna, Ekmek
**Yağ:** Yağ

# Polars DataFrame Demo

A quick demonstration of **Polars**, a fast, Rust-based DataFrame library — an alternative to pandas built for performance. Covers table creation, filtering, and grouped aggregation.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Polars](https://img.shields.io/badge/Polars-DataFrame-orange)

---

## 🇬🇧 English

### Overview
This script builds a small sample dataset, then walks through the core Polars operations: viewing a DataFrame, filtering rows by a condition, grouping by a column with an aggregation, and computing an overall summary statistic.

### Features
- DataFrame creation from a plain Python dictionary
- Row filtering with `pl.col(...)` expressions
- Grouped aggregation (`group_by` + `agg`) with sorted results
- Overall summary statistic (team-wide average)
- Structured logging via Loguru to track each step

### Requirements
- Python 3.10 or higher
- `polars`
- `loguru`

### Installation
```bash
pip install polars loguru
```

### Usage
```bash
python polars_demo.py
```

### How it works
Polars DataFrames are built on Apache Arrow and a Rust execution engine, making operations like filtering and aggregation significantly faster than pandas on larger datasets. `pl.col("department")` creates a column expression used inside `.filter()` to select matching rows. `group_by("department").agg(...)` groups the data and computes the mean code speed per group, and `.sort(...)` orders the result for readability.

---

## 🇩🇪 Deutsch

### Überblick
Dieses Skript erstellt einen kleinen Beispieldatensatz und führt anschließend durch die wichtigsten Polars-Operationen: Anzeigen eines DataFrames, Filtern von Zeilen nach einer Bedingung, Gruppieren nach einer Spalte mit Aggregation und Berechnen einer Gesamtstatistik.

### Funktionen
- DataFrame-Erstellung aus einem einfachen Python-Dictionary
- Zeilenfilterung mit `pl.col(...)`-Ausdrücken
- Gruppierte Aggregation (`group_by` + `agg`) mit sortierten Ergebnissen
- Gesamtstatistik (teamweiter Durchschnitt)
- Strukturiertes Logging über Loguru zur Nachverfolgung jedes Schritts

### Voraussetzungen
- Python 3.10 oder höher
- `polars`
- `loguru`

### Installation
```bash
pip install polars loguru
```

### Verwendung
```bash
python polars_demo.py
```

### Funktionsweise
Polars-DataFrames basieren auf Apache Arrow und einer Rust-Ausführungs-Engine, wodurch Operationen wie Filtern und Aggregation bei größeren Datensätzen deutlich schneller sind als bei pandas. `pl.col("department")` erstellt einen Spaltenausdruck, der innerhalb von `.filter()` verwendet wird, um passende Zeilen auszuwählen. `group_by("department").agg(...)` gruppiert die Daten und berechnet die durchschnittliche Code-Geschwindigkeit pro Gruppe, und `.sort(...)` ordnet das Ergebnis zur besseren Lesbarkeit.

---

## 🇹🇷 Türkçe

### Genel Bakış
Bu script küçük bir örnek veri seti oluşturur, ardından temel Polars işlemlerinden geçer: bir DataFrame'i görüntüleme, satırları bir koşula göre filtreleme, bir sütuna göre gruplayıp toplulaştırma (aggregation) yapma ve genel bir özet istatistiği hesaplama.

### Özellikler
- Düz bir Python dictionary'sinden DataFrame oluşturma
- `pl.col(...)` ifadeleriyle satır filtreleme
- Sıralanmış sonuçlarla gruplu toplulaştırma (`group_by` + `agg`)
- Genel özet istatistiği (takım geneli ortalama)
- Her adımı takip etmek için Loguru üzerinden yapılandırılmış loglama

### Gereksinimler
- Python 3.10 veya üzeri
- `polars`
- `loguru`

### Kurulum
```bash
pip install polars loguru
```

### Kullanım
```bash
python polars_demo.py
```

### Nasıl çalışır?
Polars DataFrame'leri Apache Arrow ve bir Rust çalıştırma motoru üzerine kuruludur, bu da filtreleme ve toplulaştırma gibi işlemleri büyük veri setlerinde pandas'a göre önemli ölçüde daha hızlı yapar. `pl.col("department")`, `.filter()` içinde eşleşen satırları seçmek için kullanılan bir sütun ifadesi oluşturur. `group_by("department").agg(...)` veriyi gruplar ve her grup için ortalama kod hızını hesaplar, `.sort(...)` ise sonucu okunabilirlik için sıralar.

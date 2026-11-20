# Folder Dataset (`data/`)

Folder ini digunakan untuk menyimpan 6 file dataset CSV (dari Kaggle/GitHub) yang dibaca oleh masing-masing AI Agent menggunakan `pandas` serta dianalisis di `notebooks_visdat/`.

> **Catatan Git:** Seluruh file dataset di folder ini (kecuali `README.md`) diabaikan oleh `.gitignore` agar repositori tetap ringan. Setiap anggota tim wajib mengunduh dan meletakkan file CSV secara lokal dengan **nama file persis seperti daftar di bawah**.

## Daftar 6 File CSV Wajib

| No | Nama File CSV | Modul Agent | Deskripsi Singkat |
| :-: | :--- | :--- | :--- |
| 1 | `01_hsk_vocabulary.csv` | `hsk_quiz` | Daftar kosakata HSK (Hanzi, Pinyin, arti, level HSK) untuk flashcard & kuis. |
| 2 | `02_mandarin_sentences.csv` | `sentence_translator` | Korpus pasangan kalimat Bahasa Mandarin dan terjemahannya. |
| 3 | `03_hanzi_radicals_strokes.csv` | `hanzi_stroke` | Data karakter Hanzi, radikal, jumlah goresan (*strokes*), dan komponen karakter. |
| 4 | `04_chinese_dramas_movies.csv` | `drama_recommender` | Katalog drama & film Tiongkok (judul, genre, rating, sinopsis, tahun rilis). |
| 5 | `05_chinese_culinary_menu.csv` | `culinary_menu` | Daftar menu kuliner khas Tiongkok (nama Mandarin, bahan, rasa, wilayah asal). |
| 6 | `06_ecommerce_products.csv` | `shopping_assistant` | Data produk e-commerce berbahasa Mandarin (nama produk, kategori, harga, ulasan). |

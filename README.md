# Mandarin-Learner-Agentic-AI-With-VARK
# Mandarin Agentic AI Tutor (VARK Adaptive Learning)

Sistem pembelajaran Bahasa Mandarin adaptif berbasis **Multi-Agent AI** yang secara otomatis memetakan gaya belajar pengguna menggunakan teori **VARK (Visual, Auditory, Reading/Writing, Kinesthetic)** dan menyesuaikan tingkat kesulitan kurikulum **HSK (Hanyu Shuiping Kaoshi)** secara dinamis berdasarkan analisis data interaksi.

Proyek terintegrasi ini disusun untuk memenuhi luaran akhir semester pada 4 mata kuliah:
1. **Kecerdasan Buatan**: Perancangan arsitektur Multi-Agent System (Observe, Plan, Act, Reflect).
2. **Lab Kecerdasan Buatan**: Implementasi teknis Agentic AI, integrasi LLM terstruktur, dan penyusunan *tools* berbasis dataset.
3. **Visualisasi Data Bisnis**: Exploratory Data Analysis (EDA) terhadap struktur bahasa Mandarin (HSK) dan pola perilaku belajar pengguna untuk merumuskan aturan keputusan bisnis/edukasi.
4. **Lab Visualisasi Data Bisnis**: Pembuatan *notebook* analitik, visualisasi metrik pembelajaran, serta penyajian *dashboard* wawasan data.

## Arsitektur Sistem & Alur Agentic AI

Sistem menggunakan pola **Supervisor-Worker (Orchestrator-Specialist)** di mana setiap keputusan pemilihan materi didasarkan pada hasil evaluasi riwayat belajar pengguna dan parameter dataset hasil EDA:

```mermaid
flowchart LR
    User([User]) --> FE[Frontend Web]
    FE --> Orch[Orchestrator Agent]
    Orch <--> Eval[Evaluator & Profiler Agent]
    Orch --> Vis[Visual Agent]
    Orch --> Aud[Auditory Agent]
    Orch --> Read[Reading/Writing Agent]
    Orch --> Kin[Kinesthetic Agent]
    
    Vis --- D2[(Dataset Radikal)]
    Aud --- D3[(Dataset Fonetik & Nada)]
    Read --- D4[(Dataset Korpus Kalimat)]
    Kin --- D5[(Dataset Goresan Hanzi)]
    Eval --- D6[(Dataset Log Perilaku)]

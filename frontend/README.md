# Frontend — Mandarin Ecosystem AI Hub

Folder ini merupakan **placeholder sementara** untuk aplikasi frontend sebelum stack UI diputuskan bersama oleh tim (misalnya Next.js, React + Vite, atau Streamlit).

## Integrasi Backend

Backend FastAPI menyediakan CORS terbuka untuk pengembangan lokal dan mengekspos kontrak API berikut secara default di `http://127.0.0.1:8000`:

- `GET /health`
- `POST /api/agents/hsk-quiz`
- `POST /api/agents/sentence-translator`
- `POST /api/agents/hanzi-stroke`
- `POST /api/agents/drama-recommender`
- `POST /api/agents/culinary-menu`
- `POST /api/agents/shopping-assistant`

Semua endpoint agent menerima body JSON sesuai skema `AgentRequest` (`user_input`, `filters`) dan mengembalikan JSON sesuai skema `AgentResponse` (`agent_name`, `mandarin_text`, `pinyin`, `translation`, `explanation`, `recommended_items`).

# agente

Bare-minimum Chainlit conversational AI agent.

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
DEBUG=false chainlit run app.py -w
```

Add your OpenAI API key to `.env`, then open http://localhost:8000.

If port 8000 is busy, run:

```bash
DEBUG=false chainlit run app.py -w --port 8123
```

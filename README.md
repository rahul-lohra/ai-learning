# AI Learning Lab

A Streamlit demo for learning about RAG, embeddings, and LLMs. The demo currently echoes your question; a RAG chain has not been connected yet. No API key is needed to run the demo.

## Run the app

Open a terminal and run:

```bash
cd /home/rahul/Projects/ai-learning
source .venv/bin/activate
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser. Enter a question and click **Search**.

Press **Ctrl+C** in the terminal to stop the server. Run `deactivate` to leave the virtual environment.

## Run in PyCharm

1. Choose **File > Open** and select `/home/rahul/Projects/ai-learning`.
2. Open **Settings** with **Ctrl+Alt+S** and search for **Python Interpreter**.
3. Choose **Add Interpreter > Add Local Interpreter** and select an existing environment. Browse to `/home/rahul/Projects/ai-learning/.venv/bin/python`, then apply the settings. Menu labels may vary by IDE version.
4. Select **AI Learning Lab** in the run configuration dropdown and click the green **Run** button.
5. Open the local URL printed in the Run window, usually [http://localhost:8501](http://localhost:8501). Use the red **Stop** button to stop the app.

The saved configuration is in [.run/AI Learning Lab.run.xml](.run/AI%20Learning%20Lab.run.xml). If it does not appear, open **Run > Edit Configurations**, add a **Python** configuration, and use:

| Setting | Value |
| --- | --- |
| Target type | Module name |
| Module name | `streamlit` |
| Parameters | `run app.py --server.address 127.0.0.1` |
| Working directory | `/home/rahul/Projects/ai-learning` |
| Python interpreter | `/home/rahul/Projects/ai-learning/.venv/bin/python` |

This launches the app through Streamlit. Running `app.py` directly as a Python script does not start the Streamlit web server.

Official guides: [Reuse an existing virtual environment](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html) and [Python run configurations](https://www.jetbrains.com/help/pycharm/run-debug-configuration-python.html).

## Project files

- [app.py](app.py): Streamlit application. Edit this file to change the interface or connect a RAG chain.
- [requirements.txt](requirements.txt): Direct dependencies, including Streamlit, LangChain, and ChromaDB.
- [requirements-lock.txt](requirements-lock.txt): Exact package versions saved from the installed environment.
- [.env.example](.env.example): API key placeholder for future RAG integration. Never commit real keys.
- `.venv/`: Project's local Python virtual environment.

## Set up a fresh environment

The current project already has an environment with dependencies installed. To set it up on another Ubuntu machine:

```bash
sudo apt update
sudo apt install python3-pip python3-venv
cd /path/to/ai-learning
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-lock.txt
streamlit run app.py
```

To install current dependency versions instead of the saved versions, use `python -m pip install -r requirements.txt`.

If the `streamlit` command is unavailable, activate the environment and run `python -m streamlit run app.py`.

import re
import pexpect
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse

app = FastAPI()

# Start the pm3 shell (adjust path if needed)
pm3 = pexpect.spawn('./pm3', timeout=20, encoding='utf-8')
pm3.expect(r'pm3 -->')  # Wait for prompt

def clean_ansi(text: str) -> str:
    """Remove ANSI escape sequences and clock emojis from output."""
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    text = ansi_escape.sub('', text)
    clock_emoji = re.compile(r'[\U0001F550-\U0001F567]')
    text = clock_emoji.sub('', text)
    lines = [line.rstrip() for line in text.splitlines()]
    return "\n".join(lines).strip()

def send_command(cmd: str) -> str:
    """Send a command to pm3 and get cleaned output."""
    pm3.sendline(cmd)
    pm3.expect(r'pm3 -->')
    raw_output = pm3.before
    return clean_ansi(raw_output)

@app.get("/hf/search", response_class=PlainTextResponse)
def search_hf():
    return send_command("hf search")

@app.get("/hf/mfdes/lsapp", response_class=PlainTextResponse)
def mfdes_lsapp():
    return send_command("hf mfdes lsapp --no-auth")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
      <title>Proxmark3 Commands</title>
      <style>
        body { font-family: monospace, monospace; margin: 20px; }
        #output { white-space: pre-wrap; border: 1px solid #ccc; padding: 10px; margin-top: 10px; height: 400px; overflow: auto; background: #f9f9f9; }
        button { font-size: 16px; padding: 10px 20px; margin-right: 10px; }
      </style>
    </head>
    <body>
      <h1>Proxmark3 Commands</h1>
      <button onclick="doSearch('hf/search')">Run HF Search</button>
      <button onclick="doSearch('hf/mfdes/lsapp')">Run MFDes LSApp</button>
      <pre id="output">Click a button to run a command and see output here...</pre>

      <script>
      async function doSearch(endpoint) {
        const out = document.getElementById('output');
        out.textContent = `Running ${endpoint}... please wait.`;
        try {
          const resp = await fetch('/' + endpoint);
          if (!resp.ok) {
            out.textContent = 'Error: ' + resp.statusText;
            return;
          }
          const text = await resp.text();
          out.textContent = text;
        } catch(err) {
          out.textContent = 'Fetch error: ' + err.message;
        }
      }
      </script>
    </body>
    </html>
    """

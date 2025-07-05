import re
import pexpect
from fastapi import FastAPI, Query
from fastapi.responses import PlainTextResponse, FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

pm3 = None  # global variable to hold pexpect spawn instance

# Compile regex for cleaning
ansi_escape_re = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
clock_emoji_re = re.compile(r'[\U0001F550-\U0001F567]')


def clean_output(text: str) -> str:
    text = ansi_escape_re.sub('', text)
    text = clock_emoji_re.sub('', text)
    return '\n'.join(line.rstrip() for line in text.splitlines()).strip()


def send_command(cmd: str) -> str:
    global pm3
    if pm3 is None or not pm3.isalive():
        return "Proxmark3 shell is not running. Please start it first."
    pm3.sendline(cmd)
    pm3.expect(r'pm3 -->')
    return clean_output(pm3.before)


@app.get("/", response_class=FileResponse)
def serve_home():
    return FileResponse("static/index.html")


# New endpoint to Start Proxmark3
@app.get("/start-pm3", response_class=PlainTextResponse)
def start_pm3(path: str = Query('../../proxmark3/pm3', description="Path to proxmark3 executable")):
    global pm3
    if pm3 is not None and pm3.isalive():
        return "Proxmark3 shell already running."
    try:
        pm3 = pexpect.spawn(path, timeout=20, encoding='utf-8')
        pm3.expect(r'pm3 -->')
        return f"Started Proxmark3 shell at path: {path}"
    except pexpect.ExceptionPexpect as e:
        pm3 = None
        return f"Failed to Start Proxmark3: {e}"


@app.get("/hf/search", response_class=PlainTextResponse)
def hf_search():
    return send_command("hf search")


@app.get("/hf/mfdes/info", response_class=PlainTextResponse)
def hf_mfdes_info():
    return send_command("hf mfdes info")


@app.get("/hf/mfdes/lsapp", response_class=PlainTextResponse)
def hf_mfdes_lsapp():
    return send_command("hf mfdes lsapp")


@app.get("/hf/mfdes/lsapp-no-auth", response_class=PlainTextResponse)
def hf_mfdes_lsapp_no_auth():
    return send_command("hf mfdes lsapp --no-auth")


@app.get("/hf/mfdes/get-profile", response_class=PlainTextResponse)
def hf_mfdes_get_profile():
    return send_command("hf mfdes default")


@app.get("/hf/mfdes/set-profile", response_class=PlainTextResponse)
def hf_mfdes_set_profile(
        key: str = Query(..., description="Hex key"),
        type: str = Query("AES", regex="^(DES|2TDEA|3TDEA|AES)$", description="Crypto type")
):
    cmd = f"hf mfdes default -n 0 -t {type} -k {key}"
    return send_command(cmd)


@app.get("/hf/mfdes/getappnames", response_class=PlainTextResponse)
def hf_mfdes_getappnames():
    return send_command("hf mfdes getappnames")


@app.get("/hf/mfdes/getfileids", response_class=PlainTextResponse)
def get_file_ids(aid: str):
    cmd = f"hf mfdes getfileids --aid {aid}"
    return send_command(cmd)


@app.get("/hf/mfdes/read", response_class=PlainTextResponse)
def mfdes_read(aid: str, fid: str):
    cmd = f"hf mfdes read --aid {aid} --fid {fid}"
    return send_command(cmd)

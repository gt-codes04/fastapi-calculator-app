import subprocess, time, os, signal, sys
import pytest

@pytest.fixture(scope="session", autouse=True)
def run_server():
    # Start uvicorn for E2E tests
    proc = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "app.main:app", "--port", "8000"],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    time.sleep(1.8)  # give server time to boot
    yield
    try:
        if os.name == "nt":
            proc.terminate()
        else:
            os.kill(proc.pid, signal.SIGTERM)
    except ProcessLookupError:
        pass

def test_add_via_ui(page):  # provided by pytest-playwright
    page.goto("http://127.0.0.1:8000/")
    page.fill("#a", "2")
    page.fill("#b", "3")
    page.click("#add")
    page.wait_for_selector("#out")
    assert page.inner_text("#out") == "5"

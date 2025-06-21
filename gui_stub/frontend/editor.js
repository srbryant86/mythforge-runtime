async function sendCommand(cmd) {
  const output = document.getElementById('output');
  output.innerText = 'Running: ' + cmd;
  const res = await fetch(`${API_HOST}/run`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ command: cmd })
  });
  const data = await res.text();
  output.innerText = data;
}

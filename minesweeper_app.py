import webview
import os

html_path = os.path.join(os.path.dirname(__file__), 'minesweeper.html')
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

window = webview.create_window(
    '扫雷 Minesweeper',
    html=html,
    width=900,
    height=680,
    resizable=True,
    min_size=(320, 240)
)
webview.start()

from pathlib import Path
p = Path('index.html')
text = p.read_text(encoding='utf-8')
idx = text.find('<div class="page" id="lossPage">')
print('idx', idx)
print('snippet:')
print(repr(text[idx:idx+420]))

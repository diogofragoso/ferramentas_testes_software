"""Valida arquivos referenciados por Markdown/HTML e estruturas SVG/JMX."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]


def main():
    errors = []
    count = 0
    for page in ROOT.rglob('*.md'):
        if any(part.startswith('.') for part in page.relative_to(ROOT).parts):
            continue
        text = page.read_text(encoding='utf-8')
        # Code fences may contain templates rather than repository links.
        text = re.sub(r'```.*?```', '', text, flags=re.S)
        links = re.findall(r'\]\(([^\s)]+)(?:\s+[^)]*)?\)', text)
        links += re.findall(r'(?:src|href)=["\']([^"\']+)["\']', text)
        for link in links:
            url = urlsplit(link.strip('<>'))
            if url.scheme or url.netloc or not url.path:
                continue
            count += 1
            target = (page.parent / unquote(url.path)).resolve()
            if not target.exists():
                errors.append('%s: caminho inexistente %s' % (page.relative_to(ROOT), link))
    for path in list((ROOT / 'assets').glob('*.svg')) + list((ROOT / 'exemplos/jmeter').glob('*.jmx')):
        try:
            document = ElementTree.parse(path)
            if path.suffix == '.jmx':
                for tree in document.iter('hashTree'):
                    children = list(tree)
                    if len(children) % 2 or any(children[i].tag == 'hashTree' or children[i+1].tag != 'hashTree' for i in range(0, len(children)-1, 2)):
                        errors.append('%s: par elemento/hashTree inválido' % path.name)
        except ElementTree.ParseError as error:
            errors.append('%s: XML inválido %s' % (path.name, error))
    if errors:
        print('\n'.join(errors))
        return 1
    print('OK: %s referências locais; SVGs e planos JMX bem formados.' % count)
    return 0


if __name__ == '__main__':
    sys.exit(main())

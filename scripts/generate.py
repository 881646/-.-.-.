import json
from pathlib import Path

def load_locale(lang):
    with open(f'locales/{lang}.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def generate(lang):
    template_path = Path(f'templates/{lang}_template.md')
    output_path = Path(f'examples/{lang}_safety_manual.md')
    strings = load_locale(lang)

    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()

    for key, val in strings.items():
        content = content.replace(f'{{{{{key}}}}}', val)

    output_path.write_text(content, encoding='utf-8')
    print(f'Generated {output_path}')

if __name__ == '__main__':
    for lang in ['en', 'ru']:
        generate(lang)

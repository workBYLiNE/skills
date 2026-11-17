"""Dependency-free repository checks; does not evaluate model behavior."""
from pathlib import Path
import json
import re
ROOT = Path(__file__).resolve().parents[1]

def validate(root=ROOT):
    errors=[]
    folders=sorted((root/'skills').iterdir())
    if len(folders)!=3: errors.append('Expected three skill directories')
    for folder in folders:
        file=folder/'SKILL.md'
        if not file.is_file():
            errors.append(f'Missing {file}'); continue
        text=file.read_text()
        match=re.match(r'\A---\nname: ([a-z0-9-]+)\ndescription: ([^\n]+)\n---\n',text)
        if not match:
            errors.append(f'Invalid frontmatter: {file}'); continue
        name,description=match.groups()
        if name!=folder.name or len(name)>64 or '--' in name or name.startswith('-') or name.endswith('-'):
            errors.append(f'Invalid name: {name}')
        if not 1<=len(description)<=1024: errors.append(f'Invalid description: {name}')
        for p in ('examples/input.md','examples/output.md'):
            if not (folder/p).is_file(): errors.append(f'Missing example: {name}/{p}')
    for file in root.rglob('*.md'):
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',file.read_text()):
            if '://' not in target and not target.startswith('#'):
                resolved=(file.parent/target.split('#')[0]).resolve()
                if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                    errors.append(f'Invalid local link: {file.relative_to(root)} -> {target}')
    cases=json.loads((root/'evals/cases.json').read_text())
    ids=set()
    for case in cases:
        if case['id'] in ids: errors.append('Duplicate evaluation ID')
        ids.add(case['id'])
        if not (root/'skills'/case['skill']).is_dir(): errors.append('Unknown evaluation skill')
        for key in ('input','must_include','must_not'):
            if not case.get(key): errors.append(f'Empty evaluation field: {key}')
    return errors

if __name__=='__main__':
    errors=validate()
    for error in errors: print(error)
    if errors: raise SystemExit(1)
    print('PASS: 3 skill packages; local links, metadata, examples and 9 evaluation cases checked.')

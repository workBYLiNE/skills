import importlib.util
from pathlib import Path
import json
import unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('validator',ROOT/'scripts/validate_repo.py')
validator=importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)

class RepositoryTests(unittest.TestCase):
    def test_repository_validation(self):
        self.assertEqual(validator.validate(),[])
    def test_boundary_cases_cover_all_skills(self):
        cases=json.loads((ROOT/'evals/cases.json').read_text())
        self.assertEqual(len(cases),9)
        for folder in (ROOT/'skills').iterdir():
            self.assertEqual(sum(c['skill']==folder.name for c in cases),3)
    def test_examples_are_labeled(self):
        for file in (ROOT/'skills').glob('*/examples/output.md'):
            self.assertIn('not a recorded model run',file.read_text())
    def test_validator_rejects_broken_links(self):
        import tempfile, shutil
        with tempfile.TemporaryDirectory() as directory:
            copy=Path(directory)/'repo'
            shutil.copytree(ROOT,copy,ignore=shutil.ignore_patterns('__pycache__'))
            with (copy/'README.md').open('a') as stream:
                stream.write('\n[broken](does-not-exist.md)\n')
            self.assertTrue(any('Invalid local link' in e for e in validator.validate(copy)))

if __name__=='__main__': unittest.main()

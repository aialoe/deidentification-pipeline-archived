"""Convert entity annotation from spaCy v2 TRAIN_DATA format to spaCy v3
.spacy format."""

import srsly
import typer
import warnings
from pathlib import Path

import spacy
from spacy.tokens import Doc, DocBin

if not Doc.has_extension('name'):
    Doc.set_extension('name', default=None)

def convert(lang: str, input_path: Path, output_path: Path):
    nlp = spacy.blank(lang)
    db = DocBin()
    for line in srsly.read_jsonl(input_path):
        doc = nlp.make_doc(line['data'])
        doc._.name = line['id']
        ents = []
        for start, end, label in line['label']:
            span = doc.char_span(start, end, label=label)
            if span is None:
                msg = f"Skipping entity [{start}, {end}, {label}] in the following text because the character span '{doc.text[start:end]}' does not align with token boundaries:\n\n{repr(text)}\n"
                warnings.warn(msg)
            else:
                ents.append(span)
        doc.ents = ents
        db.add(doc)
    db.to_disk(output_path)


if __name__ == "__main__":
    typer.run(convert)

# aialoe/deidentification-pipeline

<a href="https://aialoe.org/"><img src="https://aialoe.org/wp-content/uploads/2021/11/AI-ALOE-150.jpg" width="125" height="125" align="right" /></a>

This deidentification pipeline updates a named entity recognizer (NER) with labelled data from [Doccano](https://github.com/doccano/doccano). At AI-ALOE, we are developing and testing systems to obfuscate personally identifiable information (PII) from student-generated texts. The only requirement is a json lines file in the "assets" directory with labelled PII.

We have plans to extend this system using weak supervision with [skweak](https://github.com/NorskRegnesentral/skweak). We also want to  integrate our spaCy pipeline with [Microsoft Presidio](https://microsoft.github.io/presidio/), which will allow us to evaluate and combine predictions more effectively.

<a href="https://github.com/doccano/doccano"><img src="https://github.com/doccano/doccano/blob/master/frontend/assets/icon.png?raw=true" width="50" height="50" /></a>
<a href="https://github.com/NorskRegnesentral/skweak"><img src="https://raw.githubusercontent.com/NorskRegnesentral/skweak/main/data/skweak_logo.jpg" width="50" height="50"/></a>



## 🚀 Quickstart

This project is built on spaCy projects. It can be used via the
[`spacy project`](https://spacy.io/api/cli#project) CLI. To find out
more about a command, add `--help`. For detailed instructions, see the
[usage guide](https://spacy.io/usage/projects).

1. **Clone** the project.
   ```bash
   python -m spacy project clone --repo https://github.com/aloe/deidentification-pipeline
   ```
2. **Run a command** defined in the `project.yml`.
   ```bash
   python -m spacy project run init
   ```
3. **Run a workflow** of multiple steps in order.
   ```bash
   python -m spacy project run all
   ```
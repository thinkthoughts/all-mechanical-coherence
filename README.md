# all-mechanical-coherence

<p align="center">
  <img src="figures/2508-13356.png" alt="Demystifying Quantum Coherence Protection infographic" width="800">
</p>

<p align="center">
  <strong>Demystifying quantum coherence protection through lab reports, notebooks, and engineering statements inspired by arXiv:2508.13356.</strong>
</p>

**Repository description:** Lab reports and notebooks exploring all-mechanical coherence protection and fast control of silicon-vacancy spin qubits.

---

## Paper

* **Title:** All-mechanical coherence protection and fast control of a spin qubit
* **arXiv:** [2508.13356](https://arxiv.org/abs/2508.13356)
* **HTML:** [2508.13356v1](https://arxiv.org/html/2508.13356v1)

---

## Core claim

Continuous mechanical driving can create dressed spin states that protect silicon-vacancy spin qubits from low-frequency noise while remaining compatible with phononic quantum devices.

---

## Climate Reality statement

Climate reality describes what engineering prescribes: identify constraints, then build within them.

[
c = \sqrt{\frac{E}{m}}
]

---

## Notebook map

| Notebook                        | Description                                                                                                  | Colab                                                                                                                                                                                                           |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `00_context.ipynb`              | Paper metadata, engineering statements, seminar questions, and roadmap toward phonon-mediated quantum gates. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/all-mechanical-coherence/blob/main/notebooks/00_context.ipynb)              |
| `01_siv_centers.ipynb`          | Silicon-vacancy centers as optically active spin qubits in diamond.                                          | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/all-mechanical-coherence/blob/main/notebooks/01_siv_centers.ipynb)          |
| `07_spin_strain.ipynb`          | Strong spin-strain susceptibility and mechanical control.                                                    | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/all-mechanical-coherence/blob/main/notebooks/07_spin_strain.ipynb)          |
| `13_dressed_states.ipynb`       | Continuous mechanical driving and protected dressed spin states.                                             | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/all-mechanical-coherence/blob/main/notebooks/13_dressed_states.ipynb)       |
| `17_coherence_protection.ipynb` | Noise decoupling and coherence protection through mechanically dressed states.                               | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/all-mechanical-coherence/blob/main/notebooks/17_coherence_protection.ipynb) |
| `23_fast_control.ipynb`         | Ultrafast mechanically driven spin control and the reported ~800 MHz Rabi rates.                             | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/all-mechanical-coherence/blob/main/notebooks/23_fast_control.ipynb)         |
| `29_jila_seminar.ipynb`         | Seminar questions, live notes, follow-up directions, and future repo planning.                               | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/all-mechanical-coherence/blob/main/notebooks/29_jila_seminar.ipynb)         |

---

## Conceptual progression

```text
Context
    ↓
SiV spin qubit
    ↓
Spin-strain coupling
    ↓
Continuous mechanical drive
    ↓
Mechanically dressed basis
    ↓
Coherence protection
    ↓
Fast mechanical control
    ↓
Toward phonon-mediated quantum gates
```

---

## Artifacts

* Lab report: https://labreports.app/2508-13356/
* Paper metadata and engineering statements: [`paper.yaml`](paper.yaml)
* Infographic: [`figures/2508-13356.png`](figures/2508-13356.png)

---

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Open notebooks locally with Jupyter or directly in Google Colab using the buttons above.

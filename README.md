# all-mechanical-coherence

Demystifying quantum coherence protection through lab reports, notebooks, and engineering statements inspired by arXiv:2508.13356.

**Repository description:** Lab reports and notebooks exploring all-mechanical coherence protection and fast control of silicon-vacancy spin qubits.

## Paper

- **Title:** All-mechanical coherence protection and fast control of a spin qubit
- **arXiv:** [2508.13356](https://arxiv.org/abs/2508.13356)
- **HTML:** [2508.13356v1](https://arxiv.org/html/2508.13356v1)

## Core claim

Continuous mechanical driving can create dressed spin states that protect silicon-vacancy spin qubits from low-frequency noise while remaining compatible with phononic quantum devices.

## Climate Reality statement

Climate reality describes what engineering prescribes: identify constraints, then build within them.

\[
c = \sqrt{\frac{E}{m}}
\]

## Notebook map

| Notebook | Purpose |
|---|---|
| `00_context.ipynb` | Paper metadata, seminar context, abstract, and core claims. |
| `01_siv_centers.ipynb` | Silicon-vacancy centers as optically active spin qubits in diamond. |
| `07_spin_strain.ipynb` | Strong spin-strain susceptibility and mechanical control. |
| `13_dressed_states.ipynb` | Continuous mechanical driving and protected dressed spin states. |
| `17_coherence_protection.ipynb` | Noise decoupling and coherence protection. |
| `23_fast_control.ipynb` | Ultrafast mechanically driven spin control and ~800 MHz Rabi rates. |
| `29_jila_seminar.ipynb` | Seminar questions, notes, answers, and follow-up directions. |

## Artifacts

- Lab report: https://labreports.app/2508-13356/
- Paper metadata and engineering statements: [`paper.yaml`](paper.yaml)
- Infographic target: `figures/2508-13356.png`

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Open notebooks with Jupyter or upload them to Colab.

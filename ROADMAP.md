# Roadmap

## all-mechanical-coherence

This repository starts from arXiv:2508.13356, *All-mechanical coherence protection and fast control of a spin qubit*, and the related JILA seminar by Dr. Eliza Cornell.

The core result is that continuous mechanical driving can protect a silicon-vacancy spin qubit from low-frequency noise while preserving compatibility with phononic cavities. The paper also reports mechanically driven Rabi frequencies reaching approximately 800 MHz. The authors describe this as a first step toward high-fidelity, phonon-mediated quantum gates and robust on-chip quantum phononic networks.

## Phase 0 — Context

Goal: make the paper legible.

Artifacts:

- `paper.yaml`
- `notebooks/00_context.ipynb`
- `reports/labreport.md`
- `figures/2508-13356.png`

Questions:

- What is an SiV center?
- Why does spin-strain coupling matter?
- Why do phonons matter for quantum networks?
- Why is pulse-based dynamical decoupling not enough here?

## Phase 1 — Mechanism

Goal: explain the mechanism without pretending to simulate the full experiment.

Notebooks:

- `01_siv_centers.ipynb`
- `07_spin_strain.ipynb`
- `13_dressed_states.ipynb`
- `17_coherence_protection.ipynb`
- `23_fast_control.ipynb`

Working statement:

> The same mechanical interaction that enables quantum information transfer can also help preserve that information.

## Phase 2 — Seminar

Goal: use the JILA seminar to refine the repo.

Notebook:

- `29_jila_seminar.ipynb`

Seminar questions:

1. Do mechanically dressed states extend naturally to phonon-mediated two-qubit gates?
2. What currently limits the usable coherence time under continuous mechanical driving?
3. Is the next constraint mainly drive stability, heating, cavity design, material fabrication, or optical integration?
4. What would make this architecture gate-ready rather than proof-of-principle?

## Phase 3 — Toward phonon-mediated quantum gates

Goal: identify the next repo or extension.

Possible paths:

### Path A — extend this repo

Use `all-mechanical-coherence` as the parent repo for:

- dressed-state protection
- phonon-cavity compatibility
- fast single-qubit control
- gate-readiness criteria

Possible new notebooks:

- `31_gate_requirements.ipynb`
- `37_spin_phonon_bus.ipynb`
- `41_two_qubit_gate_constraints.ipynb`
- `43_error_budget.ipynb`

### Path B — create a next repo

If the seminar reveals enough gate-specific direction, start:

```text
phonon-mediated-gates

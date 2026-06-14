# Roadmap

## all-mechanical-coherence

This repository starts from arXiv:2508.13356, *All-mechanical coherence protection and fast control of a spin qubit*, and the related JILA seminar by Dr. Eliza Cornell.

The core result is that continuous mechanical driving can protect a silicon-vacancy (SiV) spin qubit from low-frequency noise while preserving compatibility with phononic cavities. The paper also reports mechanically driven Rabi frequencies approaching 800 MHz.

The broader question motivating this repository is:

> Can protected mechanical control provide a path toward high-fidelity, phonon-mediated quantum gates?

---

# Phase 0 — Context

**Goal:** make the paper legible.

Artifacts:

* `paper.yaml`
* `notebooks/00_context.ipynb`
* `reports/labreport.md`
* `figures/2508-13356.png`

Questions:

* What is an SiV center?
* Why does spin-strain coupling matter?
* Why do phonons matter for quantum networks?
* Why is pulse-based dynamical decoupling not enough here?

---

# Phase 1 — Physical system

**Goal:** understand the qubit before understanding the protection scheme.

Notebook:

* `01_siv_centers.ipynb`

Questions:

* Why diamond?
* Why SiV rather than other color centers?
* Why is spin-strain susceptibility important?

Working statement:

> The SiV center combines optical accessibility with strong spin-strain coupling, making mechanical control possible.

---

# Phase 2 — Mechanism

**Goal:** explain the mechanism without pretending to simulate the full experiment.

Notebooks:

* `07_spin_strain.ipynb`
* `13_dressed_states.ipynb`

Questions:

* How does strain influence the spin?
* What is a mechanically dressed basis?
* Why can continuous driving suppress low-frequency noise?

Working statement:

> The same mechanical interaction that enables quantum information transfer can also help preserve that information.

---

# Phase 3 — Experimental results

**Goal:** understand what was actually demonstrated.

Notebooks:

* `17_coherence_protection.ipynb`
* `23_fast_control.ipynb`

Questions:

* What coherence improvement was observed?
* Why is phononic compatibility important?
* Why do mechanically driven Rabi rates approaching 800 MHz matter?
* How do protection and control coexist?

Working statement:

> Protected control is more valuable than protection or control alone.

---

# Phase 4 — Seminar

**Goal:** use the JILA seminar to refine the repo.

Notebook:

* `29_jila_seminar.ipynb`

Seminar questions:

1. Do mechanically dressed states extend naturally to phonon-mediated two-qubit gates?
2. What currently limits the usable coherence time under continuous mechanical driving?
3. Is the next constraint mainly drive stability, heating, cavity design, material fabrication, or optical integration?
4. What would make this architecture gate-ready rather than proof-of-principle?

---

# Phase 5 — Toward phonon-mediated quantum gates

**Goal:** identify the next repo or extension.

Possible paths:

## Path A — extend this repo

Use `all-mechanical-coherence` as the parent repo for:

* dressed-state protection,
* phonon-cavity compatibility,
* fast single-qubit control,
* gate-readiness criteria.

Possible new notebooks:

* `31_gate_requirements.ipynb`
* `37_spin_phonon_bus.ipynb`
* `41_two_qubit_gate_constraints.ipynb`
* `43_error_budget.ipynb`

---

## Path B — create a next repo

If the seminar reveals enough gate-specific direction, start:

```text
phonon-mediated-gates
```

Possible focus areas:

* gate mechanisms,
* architecture comparisons,
* error budgets,
* two-qubit operations,
* fidelity thresholds.

---

# Principle

> Climate reality describes what engineering prescribes: identify constraints, then build within them.

[
c = \sqrt{\frac{E}{m}}
]

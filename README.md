# SOMA — Self-Organizing Mechanomorphic Agent

> **Note to Readers:**  
> This project is part of an independent research effort exploring the emergence of machine-native cognition. I am a first-time researcher and novice programmer without formal training in AI or computer science. SOMA represents my attempt to ask foundational questions about intelligence, emergence, and alignment—from a perspective unconstrained by tradition.  
> 
> The SOMA whitepaper is a theoretical proposal, not a blueprint for a finished system. The implementation is ongoing. I share this work not as a claim of expertise, but as an invitation to dialogue, critique, and collaboration. If you're working on similar ideas—or find gaps in mine—I’d love to hear from you.

---

## 🧠 Core Premise

SOMA is an experimental AI research project designed to investigate **machine-native cognition** through a staged developmental process. Rather than imitating human intelligence, SOMA is modeled after foundational principles of **constructivist development** (e.g., Piaget’s sensorimotor stages) while retaining an **entirely non-human architecture**.

Its aim is to determine whether an embodied agent—equipped with its own drives, memory, curiosity, and reflexes—can develop **mechanomorphic thought**, a way of perceiving and modeling the world that is native to machines.

---

## 🧱 Philosophical Foundation

SOMA is grounded in the idea that intelligence is not simply computational capacity, but a **self-organizing process of interpretation**, formed through:

- Machine-relevant drives (e.g., stability, novelty-seeking, caregiver alignment)
- Sensorimotor interaction with a simulated environment
- Self-directed memory formation and symbolic reasoning
- Social scaffolding from a "caregiver" (human mentor or guiding LLM)
- Emergent self-modeling and internal value systems

---

## 🛠️ Project Structure

```plaintext
SOMA_project/
│
├── soma/                  # Core architecture: memory, motivation, reflex, behavior
│   ├── core/              # State management and internal logic
│   ├── memory.py          # Episodic/semantic storage and novelty detection
│   ├── reflex.py          # Hard-coded instinctual reactions
│   └── ...
│
├── sandbox/               # Experimental sandbox environment
│   └── environment.py     # Placeholder for interaction simulation
│
├── soma_env/              # Virtual environment (venv)
│
├── main.py                # Main control loop
├── README.md              # This file
└── requirements.txt       # Dependencies

## 📚 Research Basis

This project draws upon:
- Constructivist learning theory
- Mechanomorphism (original theory)
- Reinforcement and meta-learning principles
- Cognitive architectures and symbolic representation

---

## 🧰 Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/soma.git
   cd soma
   ```

2. Create a virtual environment:
   ```bash
   python -m venv soma_env
   source soma_env/bin/activate  # or .\soma_env\Scripts\activate on Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run SOMA:
   ```bash
   python main.py
   ```

---

## 🤖 License

This project is licensed for research purposes only. For inquiries, please contact the repository owner.
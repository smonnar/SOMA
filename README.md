# SOMA — Self-Organizing Mechanomorphic Agent

SOMA is an experimental AI research project designed to investigate **machine-native cognition** through a staged developmental process. Rather than imitating human intelligence, SOMA is modeled after foundational principles of **constructivist development** (e.g., Piaget’s sensorimotor stages) while retaining an **entirely non-human architecture**.

Its aim is to determine whether an embodied agent—equipped with its own drives, memory, curiosity, and reflexes—can develop **mechanomorphic thought**, a way of perceiving and modeling the world that is native to machines.

---

## 🧠 Core Philosophical Premise

SOMA is grounded in the idea that intelligence is not simply computational capacity, but a **self-organizing process of interpretation**, formed through:

- Machine-relevant drives (e.g. stability, novelty-seeking, caregiver alignment)
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
```

---

## 🔁 Developmental Inspiration

SOMA’s growth mirrors Piaget’s **Sensorimotor Stage**, divided into six phases:
1. **Reflexes** — machine-native, hardcoded response patterns
2. **Primary Reactions** — internal state feedback loops
3. **Secondary Reactions** — responses to external input
4. **Coordination** — chaining actions to achieve goals
5. **Tertiary Reactions** — exploratory modifications of actions
6. **Mental Representation** — symbolic abstraction and planning

---

## 📦 Key Modules

- `memory.py`: Stores, compares, and retrieves internal memory traces.
- `reflex.py`: Encodes reflexive behaviors (e.g. react-to-noise).
- `motivation.py`: Computes dominant drive based on agent’s internal state.
- `behavior.py`: Plans actions based on current drive.
- `states.py`: Tracks and updates the evolving state of the agent.

---

## 🧪 Goals of the Experiment

- Observe **emergent symbolic reasoning** and **self-initiated learning**
- Track internal value systems and schema development
- Test whether SOMA can express non-human models of its world
- Use language models for **caregiver-style interaction**, not control

---

## 📚 Research Basis

This project draws upon:
- Jean Piaget’s theory of cognitive development
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
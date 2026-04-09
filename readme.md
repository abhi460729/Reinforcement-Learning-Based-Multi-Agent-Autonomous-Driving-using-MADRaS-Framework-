# 🚗 Reinforcement Learning-Based Autonomous Driving using MADRaS

## 📌 Overview

This project demonstrates autonomous driving using Reinforcement Learning in a multi-agent environment. The system is built using the MADRaS framework on top of the TORCS simulator.

The objective is to train an AI agent (ego vehicle) to drive safely and efficiently under different traffic conditions.

---

## 🧠 Key Concepts

* Reinforcement Learning (RL)
* Multi-Agent Systems
* Autonomous Driving
* Reward Engineering

---

## 🏗️ Tech Stack

* Python 3
* MADRaS Framework
* TORCS Simulator
* Stable-Baselines3 (PPO)

---

## ⚙️ System Architecture

TORCS (Simulation Environment)
↓
MADRaS (RL Interface Layer)
↓
Custom RL Agent (PPO)
↓
Action → Steering, Throttle
↓
Environment Response → Observation + Reward

---

## 📁 Project Structure

madras_project/
│
├── config.py
├── reward.py
├── utils.py
├── env.py
├── train.py
├── evaluate_no_traffic.py
├── evaluate_medium_traffic.py
├── evaluate_heavy_traffic.py
├── plot_results.py
└── models/

---

## 🚀 Installation (GCP / Ubuntu)

### Step 1: Update system

```bash
sudo apt update && sudo apt upgrade -y
```

### Step 2: Install dependencies

```bash
sudo apt install git build-essential python3-pip -y
pip3 install stable-baselines3 matplotlib numpy
```

### Step 3: Install MADRaS

```bash
git clone https://github.com/madras-simulator/MADRaS.git
cd MADRaS
pip3 install -e .
```

### Step 4: Install TORCS

(Follow TORCS installation steps)

---

## ▶️ Running the Project

### Step 1: Start TORCS

```bash
torcs
```

---

### Step 2: Train the Agent

```bash
python3 train.py
```

---

### Step 3: Run Scenarios

#### 🟢 Scenario 1: No Traffic

```bash
python3 evaluate_no_traffic.py
```

#### 🟡 Scenario 2: Medium Traffic

(Add 3 cars in TORCS GUI)

```bash
python3 evaluate_medium_traffic.py
```

#### 🔴 Scenario 3: Heavy Traffic

(Add 6–8 cars in TORCS GUI)

```bash
python3 evaluate_heavy_traffic.py
```

---

## 🧪 Scenarios Description

### 1. No Traffic

* Single vehicle
* High speed, smooth driving

### 2. Medium Traffic

* 3–4 vehicles
* Adaptive behavior
* Collision avoidance

### 3. Heavy Traffic

* 6–8 vehicles
* Slower, cautious navigation
* Complex decision-making

---

## 🎯 Reward Function

The reward is designed to encourage:

* High speed
* Staying on track
* Avoiding collisions
* Maintaining correct orientation

---

## 📊 Expected Results

| Scenario       | Behavior       |
| -------------- | -------------- |
| No Traffic     | Fast, smooth   |
| Medium Traffic | Balanced       |
| Heavy Traffic  | Safe, cautious |

---

## 🧠 Key Observations

* The agent adapts behavior based on traffic density
* Reward design significantly impacts learning
* Multi-agent environments improve realism

---

## 🔥 Future Improvements

* Multi-agent RL (multiple learning vehicles)
* Advanced reward shaping
* Real-world dataset integration
* Sensor fusion

---

## 🧑‍💻 Author

* Autonomous Driving RL Project

---

## 📌 Conclusion

This project demonstrates how reinforcement learning can be used to train autonomous vehicles in increasingly complex environments. The results highlight the adaptability of RL agents in multi-agent traffic scenarios.

---

## 📜 License

This project is for educational and research purposes.

# 📱 On-Device LLM Inference with LoRA-Tuned Qwen2.5-3B

This project documents an end-to-end experiment in running a **LoRA fine-tuned 3B parameter language model entirely on a smartphone**, fully offline.

The workflow covers:
- Fine-tuning a large pretrained model using LoRA
- Converting models to GGUF for efficient inference
- Deploying and running inference on an Android device via Termux
- Measuring real-world latency and throughput on mobile hardware

The goal was not benchmarking perfection, but to **validate the practicality of small-to-mid scale LLMs (2–4B) for real on-device use**.

---

## 🔍 What This Project Covers

- Downloaded the **Qwen2.5-3B-Instruct** base model from Hugging Face
- Fine-tuned it using **LoRA** on instruction-style datasets
- Converted both the base and LoRA-adapted models into **GGUF format**
- Deployed the model to an Android phone
- Ran inference using `llama-cli` from **llama.cpp**
- Collected and analyzed latency logs from real executions

All inference was done **offline**, without cloud APIs or GPU acceleration.

---

## 🧠 Model & Training Details

**Base Model**
- Qwen2.5-3B-Instruct

**Fine-Tuning Method**
- LoRA on FP16 base weights
- Training stack: Unsloth + Hugging Face Transformers
- Experiment tracking: Weights & Biases

**Training Data**
- **GPTeacher** — instruction-following and reasoning-oriented data  
- **Dolly 15K** — general-purpose conversational and task prompts  

**Why this dataset mix?**  
To improve instruction adherence, reasoning quality, and conversational behavior while keeping the model lightweight enough for mobile inference.

---

## 📱 Mobile Deployment Setup

**Device**
- Chipset: MediaTek Dimensity 8200  
- RAM: 12 GB + 8 GB extended  

**Inference Stack**
- Environment: Termux (Android)
- Backend: `llama-cli` (llama.cpp)
- Model format: GGUF (Q4_K_M quantization)

---

## ⚙️ Build & Conversion Workflow

### 1️⃣ Clone and build llama.cpp

```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
make -j
```
# 📱 On-Device LLM Inference with LoRA-Tuned Qwen2.5-3B

This project documents an end-to-end experiment in running a **LoRA fine-tuned 3B parameter language model entirely on a smartphone**, fully offline.

The workflow covers:
- Fine-tuning a large pretrained model using LoRA
- Converting models to GGUF for efficient inference
- Deploying and running inference on an Android device via Termux
- Measuring real-world latency and throughput on mobile hardware

The goal was not benchmarking perfection, but to **validate the practicality of small-to-mid scale LLMs (2–4B) for real on-device use**.

---

## 🔍 What This Project Covers

- Downloaded the **Qwen2.5-3B-Instruct** base model from Hugging Face
- Fine-tuned it using **LoRA** on instruction-style datasets
- Converted both the base and LoRA-adapted models into **GGUF format**
- Deployed the model to an Android phone
- Ran inference using `llama-cli` from **llama.cpp**
- Collected and analyzed latency logs from real executions

All inference was done **offline**, without cloud APIs or GPU acceleration.

---

## 🧠 Model & Training Details

**Base Model**
- Qwen2.5-3B-Instruct

**Fine-Tuning Method**
- LoRA on FP16 base weights
- Training stack: Unsloth + Hugging Face Transformers
- Experiment tracking: Weights & Biases

**Training Data**
- **GPTeacher** — instruction-following and reasoning-oriented data  
- **Dolly 15K** — general-purpose conversational and task prompts  

**Why this dataset mix?**  
To improve instruction adherence, reasoning quality, and conversational behavior while keeping the model lightweight enough for mobile inference.

---

## 📱 Mobile Deployment Setup

**Device**
- Chipset: MediaTek Dimensity 8200  
- RAM: 12 GB + 8 GB extended  

**Inference Stack**
- Environment: Termux (Android)
- Backend: `llama-cli` (llama.cpp)
- Model format: GGUF (Q4_K_M quantization)

---

## ⚙️ Build & Conversion Workflow

### 1️⃣ Clone and build llama.cpp

```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
make -j
```
This builds llama-cli and the conversion utilities.

2️⃣ Convert base Hugging Face model to GGUF
```
python convert_hf_to_gguf.py \
  --model-path /path/to/Qwen2.5-3B-Instruct \
  --outfile qwen2.5-3b-base.gguf \
  --outtype q4_k_m
```
This converts the original safetensors weights into a quantized GGUF file suitable for mobile inference.

3️⃣ Convert LoRA adapter to GGUF
```
python convert_lora_to_gguf.py \
  --base qwen2.5-3b-base.gguf \
  --lora-path /path/to/lora_adapter \
  --outfile qwen2.5-3b-lora.gguf
```

This merges the LoRA adapter into the base GGUF model.

4️⃣ Deploy to Android (Termux)
After connecting with mobile:
```
cp qwen2.5-3b-lora.gguf /data/data/com.termux/files/home/
```

5️⃣ Run inference using llama-cli
```
./llama-cli \
  -m qwen2.5-3b-lora.gguf \
  -p "Explain transformers in simple terms." \
  -n 200 \
  --temp 0.8 \
  --top-p 0.9 \
  --top-k 40
```

All inference runs entirely on-device, using CPU only.

All inference runs entirely on-device, using CPU only.

### ⚡ Observed Performance (llama-cli logs)

**Prompt Evaluation**

907.77 ms / 20 tokens

~45.29 ms per token

~22.08 tokens/sec

**Generation**

68,574.68 ms / 703 tokens

~97.55 ms per token

~10.25 tokens/sec

For a 3B parameter Transformer running purely on a smartphone CPU, achieving ~10 tokens/sec is a strong result.

### 🎯 Key Takeaways

Models in the 2–4B range are already practical for real-world, on-device AI

LoRA enables meaningful customization without retraining full models

GGUF + llama.cpp make mobile inference viable today

**Offline inference offers:**

Zero cloud dependency

Full privacy

Predictable latency

Complete control over the model

This project reinforces that edge AI is no longer theoretical — it is already usable with the right tooling and model sizes.

### 📂 Repository Scope

This repository focuses on:

- Model downloading

- LoRA fine-tuning workflow

- GGUF conversion

- Mobile deployment and inference

- Performance observation

It is intended as a practical reference, not a production framework.


### 📄 License

This project is shared for educational and experimental purposes.
Refer to the base model and dataset licenses for usage constraints.

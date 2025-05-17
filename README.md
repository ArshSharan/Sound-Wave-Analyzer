# 🔊 Sound Wave Analyzer

![banner](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b?style=for-the-badge&logo=streamlit)
![status](https://img.shields.io/badge/Status-Working-green?style=for-the-badge)

A futuristic, hacker-themed web tool that lets you **upload audio files (WAV format)** and visualize both the **waveform** and the **real-time spectrogram** of the audio. Perfect for audio analysis, signal processing students, CTF enthusiasts, or anyone curious about how sound behaves visually.

---

## ⚡ Features

- [ ] Upload `.wav` audio files
- [ ] View detailed **waveform plots** (amplitude vs. time)
- [ ] See a **real-time animated spectrogram** (frequency vs. time)
- [ ] Fully browser-based – no installation required
- [ ] Built with 🎧 Streamlit + NumPy + SciPy + Matplotlib
- [ ] Compatible with embedding via `<iframe>`

---

## 🚀 Demo

**Live App:** [Click here to launch](https://sound-wave-analyzer.streamlit.app/)

*(hosted via Streamlit, embeddable in any platform)*

---

## 🎯 Use Cases

- Audio steganography analysis
- Spectral pattern inspection
- CTF and InfoSec audio-related challenges
- Educational tool for learning sound signal properties
- Visualizing how speech or music looks in frequency domain

---

## 🧠 How It Works

- Uses `numpy` and `scipy` to process the WAV file and extract audio data
- Visualizes:
  - **Waveform**: a time-domain plot of the amplitude of the sound
  - **Spectrogram**: a frequency-time representation using STFT (Short-Time Fourier Transform)
- Streamlit handles the interactive UI and animations

---

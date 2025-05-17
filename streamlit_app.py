import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import wave
import io
import librosa
import librosa.display
from streamlit_extras.stylable_container import stylable_container

# ---- CSS ---- #
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;900&family=Rajdhani:wght@400;700&display=swap');

:root {
    --primary: #00f0ff;
    --secondary: #ff00ff;
    --dark: #0a0a12;
    --light: #f0f0ff;
    --accent: #7b2dff;
}

html, body, [class*="css"] {
    font-family: 'Rajdhani', sans-serif;
    background-color: var(--dark);
    color: var(--light);
}

h1, h2, h3 {
    font-family: 'Orbitron', sans-serif;
    color: var(--primary) !important;
    text-shadow: 0 0 10px rgba(0, 240, 255, 0.6);
    letter-spacing: 2px;
}

.stApp {
    background-color: var(--dark);
    background-image: radial-gradient(circle at 30% 40%, rgba(123, 45, 255, 0.08), transparent 30%),
                      radial-gradient(circle at 80% 70%, rgba(0, 240, 255, 0.08), transparent 30%);
}

.stFileUploader > div > div {
    border: 2px dashed var(--primary);
    background: rgba(10, 10, 20, 0.5);
    border-radius: 10px;
}

.stButton > button {
    border: 2px solid var(--primary);
    background: transparent;
    color: var(--primary);
    font-family: 'Orbitron';
    font-weight: bold;
    border-radius: 5px;
}

.audio-player {
    margin: 20px 0;
}

.ascii-art {
    font-family: monospace;
    color: var(--accent);
    text-align: center;
    white-space: pre;
    line-height: 1.1;
    margin-bottom: -10px;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

# ---- ASCII ART HEADER ---- #
ascii_art = r"""
   ________  ______  __________ _    ____________  _____ ______
  / ____/\ \/ / __ )/ ____/ __ \ |  / / ____/ __ \/ ___// ____/
 / /      \  / __  / __/ / /_/ / | / / __/ / /_/ /\__ \/ __/   
/ /___    / / /_/ / /___/ _, _/| |/ / /___/ _, _/___/ / /___   
\____/   /_/_____/_____/_/ |_| |___/_____/_/ |_|/____/_____/   
"""

        # ---- MAIN UI ---- #
st.markdown(f"""
        <div style="text-align: center; margin-bottom: 30px;">
            <div class="ascii-art" style="color: var(--primary); font-size: 10px; opacity: 0.8; white-space: pre;">{ascii_art}</div>
            <h1 class="glow" style="margin-top: -10px; font-size: 3em;">SOUND WAVE ANALYZER</h1>
            <p style="color: var(--light); letter-spacing: 2px;">WAVEFORM • FFT • SPECTROGRAM ANALYSIS</p>
            <div style="height: 2px; background: linear-gradient(90deg, transparent, var(--primary), transparent); margin: 10px auto; width: 50%;"></div>
        </div>
        """, unsafe_allow_html=True)
audio_file = st.file_uploader("Upload a WAV/MP3 Audio File", type=["wav", "mp3"])

# ---- ANALYSIS ---- #
if audio_file:
    st.audio(audio_file, format='audio/wav', start_time=0)

    # Load audio
    y, sr = librosa.load(audio_file, sr=None)

    st.markdown("## 📈 Waveform")
    fig, ax = plt.subplots(figsize=(10, 3))
    librosa.display.waveshow(y, sr=sr, ax=ax, color='#00f0ff')
    ax.set(title='Waveform')
    st.pyplot(fig)

    st.markdown("## 🎛️ Frequency Spectrum (FFT)")
    fft = np.fft.fft(y)
    freq = np.fft.fftfreq(len(fft), 1/sr)
    magnitude = np.abs(fft)

    fig2, ax2 = plt.subplots(figsize=(10, 3))
    ax2.plot(freq[:len(freq)//2], magnitude[:len(magnitude)//2], color='#7b2dff')
    ax2.set(title='Frequency Spectrum', xlabel='Frequency (Hz)', ylabel='Amplitude')
    st.pyplot(fig2)

    st.markdown("## 🔮 Live-style Spectrogram")
    fig3, ax3 = plt.subplots(figsize=(10, 4))
    S = librosa.stft(y)
    S_db = librosa.amplitude_to_db(np.abs(S), ref=np.max)
    img = librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='log', ax=ax3, cmap='magma')
    fig3.colorbar(img, ax=ax3, format="%+2.f dB")
    ax3.set(title='Spectrogram')
    st.pyplot(fig3)

# ---- FOOTER ---- #
st.markdown("""
<div style="text-align: center; margin-top: 50px; color: var(--light); font-size: 0.8em; opacity: 0.6;">
    CYBERVERSE TOOL v1.0 | [STATUS: LIVE] | [ANALYZER READY]
</div>
""", unsafe_allow_html=True)

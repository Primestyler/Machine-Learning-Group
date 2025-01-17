import streamlit as st
import librosa
from concurrent.futures import ProcessPoolExecutor, as_completed
import numpy as np
import pandas as pd
from sklearn.decomposition import NMF
from sklearn.preprocessing import normalize, MinMaxScaler
import os

def extract_features(file_path, sr=22050):
    """Extract features from an audio file.
    """
    
    try:
        y, sr = librosa.load(file_path, sr=sr)

        spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
        spectral_centroid_mean = np.mean(spectral_centroid)

        spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)
        spectral_bandwidth_mean = np.mean(spectral_bandwidth)
        
        spectral_contrast = librosa.feature.spectral_contrast(y=y, sr=sr)
        spectral_contrast_mean = np.mean(spectral_contrast)

        zcr = librosa.feature.zero_crossing_rate(y)
        zcr_mean = np.mean(zcr)

        rms = librosa.feature.rms(y=y)
        rms_mean = np.mean(rms)

        rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr, roll_percent=0.85)
        rolloff_mean = np.mean(rolloff)

        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        mfcc_means = [np.mean(coeff) for coeff in mfcc]
        
        chroma = librosa.feature.chroma_stft(y=y, sr=sr)
        chroma_means = [np.mean(chroma_coeff) for chroma_coeff in chroma]

        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

        contrast = librosa.feature.spectral_contrast(y=y, sr=sr)
        contrast_means = [np.mean(band) for band in contrast]

        tonnetz = librosa.feature.tonnetz(y=y, sr=sr)
        tonnetz_means = [np.mean(axis) for axis in tonnetz]

        flatness = librosa.feature.spectral_flatness(y=y)
        flatness_mean = np.mean(flatness)

        features = {
            'spectral_centroid': spectral_centroid_mean,
            'spectral_bandwidth': spectral_bandwidth_mean,
            'spectral_contrast': spectral_contrast_mean,
            'zero_crossing_rate': zcr_mean,
            'rms': rms_mean,
            'spectral_rolloff': rolloff_mean,
            'mfcc_mean_1': mfcc_means[0],
            'mfcc_mean_2': mfcc_means[1],
            'mfcc_mean_3': mfcc_means[2],
            'mfcc_mean_4': mfcc_means[3],
            'mfcc_mean_5': mfcc_means[4],
            'mfcc_mean_6': mfcc_means[5],
            'mfcc_mean_7': mfcc_means[6],
            'mfcc_mean_8': mfcc_means[7],
            'mfcc_mean_9': mfcc_means[8],
            'mfcc_mean_10': mfcc_means[9],
            'mfcc_mean_11': mfcc_means[10],
            'mfcc_mean_12': mfcc_means[11],
            'mfcc_mean_13': mfcc_means[12],
            'chroma_mean_1': chroma_means[0],
            'chroma_mean_2': chroma_means[1],
            'chroma_mean_3': chroma_means[2],
            'chroma_mean_4': chroma_means[3],
            'chroma_mean_5': chroma_means[4],
            'chroma_mean_6': chroma_means[5],
            'chroma_mean_7': chroma_means[6],
            'chroma_mean_8': chroma_means[7],
            'chroma_mean_9': chroma_means[8],
            'chroma_mean_10': chroma_means[9],
            'chroma_mean_11': chroma_means[10],
            'chroma_mean_12': chroma_means[11],
            'tempo': tempo[0],
            'contrast_mean_1': contrast_means[0],
            'contrast_mean_2': contrast_means[1],
            'contrast_mean_3': contrast_means[2],
            'contrast_mean_4': contrast_means[3],
            'contrast_mean_5': contrast_means[4],
            'contrast_mean_6': contrast_means[5],
            'contrast_mean_7': contrast_means[6],
            'tonnetz_mean_1': tonnetz_means[0],
            'tonnetz_mean_2': tonnetz_means[1],
            'tonnetz_mean_3': tonnetz_means[2],
            'tonnetz_mean_4': tonnetz_means[3],
            'tonnetz_mean_5': tonnetz_means[4],
            'tonnetz_mean_6': tonnetz_means[5],
            'flatness_mean': flatness_mean
        }

        return features

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def append_audio_features(df, file_path):
    features = extract_features(file_path)
    if features:
        features['filename'] = file_path
        df = pd.concat([df, pd.DataFrame([features])], ignore_index=True)
    return df

def recommend_top_5(df, norm_features, target_index):
    target_vector = norm_features.iloc[target_index].values
    similarities = norm_features.iloc[:-1].values @ target_vector
    top_5_indices = np.argsort(similarities)[-5:][::-1]
    return df.iloc[top_5_indices]

@st.cache_data
def load_initial_data(file_list):
    feature_array = []

    for file in file_list:
        try: 
            features = extract_features(os.path.join('Datasets/unlabeled', file))
            if features:
                features['filename'] = os.path.join('Datasets/unlabeled', file)
                feature_array.append(features)
            
        except Exception as e:
            print(f"Error loading {file}: {e}")
                
    df = pd.DataFrame(feature_array)
    return df

st.title('Audio Recommendation System')

df = load_initial_data(os.listdir('Datasets/unlabeled'))

if st.checkbox('Show database'):
    st.dataframe(df)
    
uploaded_file = st.file_uploader("Upload a .wav file", type='wav')

if uploaded_file:
    with open('temp.wav', 'wb') as f:
        f.write(uploaded_file.read())
        
    st.write('Extracting features...')
    df = append_audio_features(df, 'temp.wav')
    
    st.write('Finding recommendations...')
    df_scaled = MinMaxScaler((1, 2)).fit_transform(df.drop(columns='filename', errors='ignore'))
    nmf = NMF(n_components=3)
    nmf_features = nmf.fit_transform(df_scaled)
    norm_features = pd.DataFrame(normalize(nmf_features, axis=0))
    
    recommendations = recommend_top_5(df, norm_features, target_index=len(df) - 1)
    st.write('**Uploaded Audio File**')
    st.audio('temp.wav')
    
    st.write('Top 5 similar audio files:')
    for _, row in recommendations.iterrows():
        st.write(f'Audio File: {os.path.basename(row["filename"])}')
        st.audio(row['filename'])
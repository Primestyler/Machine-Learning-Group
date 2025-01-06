import librosa
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import os
from concurrent.futures import ProcessPoolExecutor, as_completed

class DataLoader:
    @staticmethod
    def extract_features(file_path, sr=22050):
        """Extract features from an audio file.
        
        Parameters
        ----------
        file_path : str
            Path to the audio file
        sr : int, optional
            Sampling rate, by default 22050
            
        Returns
        -------
        dict
            Dictionary containing the extracted features
        """
        
        try:
            y, sr = librosa.load(file_path, sr=sr)

            spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
            spectral_centroid_mean = np.mean(spectral_centroid)

            spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)
            spectral_bandwidth_mean = np.mean(spectral_bandwidth)

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
                'zero_crossing_rate': zcr_mean,
                'rms': rms_mean,
                'spectral_rolloff': rolloff_mean,
                'mfcc_mean_1': mfcc_means[0],
                'mfcc_mean_2': mfcc_means[1],
                'mfcc_mean_3': mfcc_means[2],
                'chroma_mean_1': chroma_means[0],
                'chroma_mean_2': chroma_means[1],
                'tempo': tempo,
                'contrast_mean_1': contrast_means[0],
                'contrast_mean_2': contrast_means[1],
                'tonnetz_mean_1': tonnetz_means[0],
                'tonnetz_mean_2': tonnetz_means[1],
                'flatness_mean': flatness_mean
            }

            return features

        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return None

    def featureDataFrame(self, file_list, base_dir, max_workers=6):
        """Extract features from a list of audio files and return a DataFrame.
        
        Parameters
        ----------
        file_list : list
            List of audio files
        base_dir : str
            Base directory where the audio files are located
        max_workers : int, optional
            Number of workers to use, by default 6
            
        Returns
        -------
        pd.DataFrame
            DataFrame containing the extracted features
        """
        feature_array = []

        with ProcessPoolExecutor(max_workers=max_workers) as executor:
            future_to_file = {
                executor.submit(self.extract_features, os.path.join(base_dir, file)): file
                for file in file_list
            }

            for future in as_completed(future_to_file):
                file_name = future_to_file[future]
                try:
                    features = future.result()
                    if features:
                        features["filename"] = file_name
                        feature_array.append(features)
                except Exception as e:
                    print(f"Error loading {file_name}: {e}")

        return pd.DataFrame(feature_array)
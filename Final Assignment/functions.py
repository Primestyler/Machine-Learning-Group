import librosa
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import os
from concurrent.futures import ProcessPoolExecutor, as_completed

class DataLoader:
    def get_data(self, file_list: list, path: str, max_workers: int = 6) -> pd.DataFrame:
        """Creates a dataframe from a list of files

        Parameters
        ----------
        file_list : list
            list of filenames
        path : str
            path to the files
        max_workers : int, optional
            number of workers to use, by default 6

        Returns
        -------
        pandas.DataFrame
            dataframe containing the data from the files

        Raises
        ------
        TypeError
            file_list must be a list of strings
        TypeError
            file_list must contain only strings
        TypeError
            path must be a string
        """    

        if not isinstance(file_list, list):
            raise TypeError('file_list must be a list of strings')
        if not all(isinstance(file, str) for file in file_list):
            raise TypeError('file_list must contain only strings')
        if not isinstance(path, str):
            raise TypeError('path must be a string')
        if not isinstance(max_workers, int):
            print('max_workers must be an integer, defaulting to 6')
            max_workers = 6

        dataframes = {}
        max_length = 0

        with ProcessPoolExecutor(max_workers=max_workers) as executor:
            future_to_file = {executor.submit(self._load_data, file, path): file for file in file_list}
            
            for future in as_completed(future_to_file):
                file = future_to_file[future]
                try:
                    data, _ = future.result()
                    dataframes[file] = data
                    max_length = max(max_length, len(data))
                except FileNotFoundError:
                    print(f'File {file} not found')
                except Exception as e:
                    print(f'Error loading {file}: {e}')
                    
        for file, data in dataframes.items():
            if len(data) < max_length:
                dataframes[file] = np.pad(data, (0, max_length - len(data)), constant_values=np.nan)
                
        return pd.DataFrame(dataframes)
    
    def _load_data(self, file_name: str, path: str) -> tuple:
        """Load labeled data from a file

        Parameters
        ----------
        file_name : str
            The name of the file to load the data from
        path : str
            The path to the file

        Returns
        -------
        tuple
            A tuple containing the audio data and the sample

        Raises
        ------
        TypeError
            If the file_name is not a string
        TypeError
            If the path is not a string
        FileNotFoundError
            If the file is not found
        """    
        
        if not isinstance(file_name, str):
            raise TypeError('file_name must be a string')
        if not isinstance(path, str):
            raise TypeError('path must be a string')
        
        path = Path(path) / file_name
        
        if not path.is_file():
            raise FileNotFoundError(f'File {file_name} does not exist at {path}')
        
        y, sr = librosa.load(path, sr=22050)

        return y, sr
    
    def extract_features(file_path, sr=22050):

        y, sr = librosa.load(file_path, sr=22050)

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

def featureDataFrame(file_list, base_dir):
    feature_array = []
    for file_name in file_list:

        audio_path = os.path.join(base_dir, file_name)
        features = DataLoader.extract_features(audio_path)
        if features is not None:
            features["filename"] = file_name
            feature_array.append(features)

    return pd.DataFrame(feature_array)

class Visualizer:
    def __init__(self, data: pd.DataFrame, title: str, rows: int, cols: int, figsize: tuple = (20, 20)):
        """Initializer for the Visualizer class

        Parameters
        ----------
        data : pd.DataFrame
            Data to be visualized
        title : str
            Title of the visualization
        rows : int
            Number of rows
        cols : int
            Number of columns
        figsize : tuple, optional
            Size of the figure to be plotted, by default (20, 20)

        Raises
        ------
        ValueError
            Data must be a pandas DataFrame
        ValueError
            Title must be a string
        ValueError
            Rows must be an integer
        ValueError
            Cols must be an integer
        ValueError
            Figsize must be a tuple
        """        
        
        if not isinstance(data, pd.DataFrame):
            raise ValueError('Data must be a pandas DataFrame')
        if not isinstance(title, str):
            raise ValueError('Title must be a string')
        if not isinstance(rows, int):
            raise ValueError('Rows must be an integer')
        if not isinstance(cols, int):
            raise ValueError('Cols must be an integer')
        if not isinstance(figsize, tuple):
            raise ValueError('Figsize must be a tuple')
        
        self.data = data
        self.title = title
        self.rows = rows
        self.cols = cols
        self.figsize = figsize
        
    def subplots(self):
        """Plot subplots of the data
        """        
        
        fig, axes = plt.subplots(self.rows, self.cols, figsize=self.figsize)
        
        axes = axes.flatten()
        
        for i, file in enumerate(self.data.columns):
            axes[i].plot(self.data[file])
            axes[i].set_title(file)
            axes[i].axis('off')
        
        plt.suptitle(self.title, fontsize=24, y=1.00)
        plt.tight_layout()
        plt.show()
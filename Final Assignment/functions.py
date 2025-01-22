import librosa
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os
from concurrent.futures import ProcessPoolExecutor, as_completed
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA, NMF
import datetime
from sklearn.preprocessing import normalize

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

def visualize_feature(feature, df):
    avg_value = df.groupby('genre')[feature].mean().reset_index()

    plt.figure(figsize=(5, 5))
    plt.scatter(avg_value['genre'], avg_value[feature], color='red', s=50)
    for idx, row in avg_value.iterrows():
        plt.text(row['genre'], row[feature] + 0.02 * row[feature], f"{row['genre']}", ha='center', fontsize=9)

    plt.xlabel('Genre')
    plt.xticks(ticks=[])
    plt.ylabel(f'Avg {feature}')
    plt.yticks(ticks=[])
    plt.title(f'Avg {feature} by Genre')
    plt.show()

def visualize_feature_multiline(df,feature_prefix, num_sub_features, x_col='genre', x_label='Genre', y_label='Feature Value', title='Feature Plot',figsize=(10, 6)):
    
    plt.figure(figsize=figsize)

    x_values = df[x_col].unique()
    for i in range(num_sub_features):
        col_name = f"{feature_prefix}{i+1}"
        avg_values = df.groupby(x_col)[col_name].mean().reindex(x_values)
        plt.plot(x_values, avg_values, marker='o', label=col_name)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


class KMeansClustering:
    def __init__(self, unlabeled_data, unlabled_df):
        self.unlabeled_data = unlabeled_data
        self.unlabeled_df = unlabled_df
        
    def finding_k(self, k_range):
        inertia = []
        
        for k in range(k_range[0], k_range[1]):
            kmeans = KMeans(n_clusters=k, random_state=42)
            kmeans.fit(self.unlabeled_data)
            inertia.append(kmeans.inertia_)
            
        self._plot_elbow(k_range, inertia)
        
    def create_kmeans(self, k):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(self.unlabeled_data)
        self.unlabeled_df['cluster'] = kmeans.labels_
        
        return self.unlabeled_df
    
    def cluster_to_genre(self, genre_mapping):
        self.unlabeled_df['genre'] = self.unlabeled_df['cluster'].map(genre_mapping)
    
    def create_submission(self):
        submission = self.unlabeled_df[['filename', 'genre']]
        submission.to_csv(f'Datasets/submission_{datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")}.csv', index=False)
    
    def _plot_elbow(self, k_range, inertia):
        plt.figure(figsize=(10, 5))
        plt.plot(range(k_range[0], k_range[1]), inertia, marker='o')
        plt.title('Elbow Method')
        plt.xlabel('Number of clusters')
        plt.ylabel('Inertia')
        plt.show()
        
    def _map_clusters_to_genres(self):
        cluster_genre_mapping = (self.labeled_df.groupby('cluster')['genre'].agg(lambda x:x.mode()[0]).to_dict())
        
        return cluster_genre_mapping
    
class PostClusteringVisualizations:
    def __init__(self, clustered_df, labeled_df):
        self.clustered_df = clustered_df
        self.labeled_df = labeled_df
        self.genres = self.labeled_df['genre'].unique()
        
    def scatter_plot(self, col1, col2):
        fig, axes = plt.subplots(5, 2, figsize=(10, 20))
        axes = axes.flatten()
        
        for i, genre in enumerate(self.genres):
            ax = axes[i]
            genre_df = self.labeled_df[self.labeled_df['genre'] == genre]
            
            sns.scatterplot(data=genre_df, x=col1, y=col2, color='red', ax=ax, label=f'Genre: {genre}')
            sns.scatterplot(data=self.clustered_df, x=col1, y=col2, hue='cluster', palette='viridis', marker='o', ax=ax)
            
            red_patch = mpatches.Patch(color='red', label=f'Genre: {genre}')
            handles, lables = ax.get_legend_handles_labels()
            
            ax.set_title(genre)
            
        for j in range(len(self.genres), len(axes)):
            fig.delaxes(axes[j])
            
        fig.suptitle(f'Clustered Data and Genre Comparison: {col1} vs {col2}', fontsize=16)
        plt.tight_layout(rect=[0, 0, 1, 0.99])
        plt.show()
        
class PCAReduction:
    def __init__(self, df):
        self.df = df
        
    def find_n(self):
        self.pca = PCA()
        self.pca.fit(self.df)
        
        self.explained_variance = self.pca.explained_variance_ratio_
        self.features = range(self.pca.n_components_)
        
        self._plot_variance()
        
    def reduction(self, n):
        self.pca = PCA(n_components=n)
        self.df_reduced = self.pca.fit_transform(self.df)
        
        return self.df_reduced
    
    def reduce_labeled(self, labeled_df):
        self.labeled_df = labeled_df
        self.df_reduced_labeled = self.pca.transform(self.labeled_df)
        
        return self.df_reduced_labeled
    
    def _plot_variance(self):
        plt.figure(figsize=(10,6))
        plt.bar(self.features, self.explained_variance)
        plt.xlabel('PCA components')
        plt.ylabel('Variance')
        plt.xticks(self.features)
        plt.show()
        
class NMFReduction:
    def __init__(self, data):
        self.data = data
        self.nmf = NMF(n_components=3)
        
    def reduction(self):
        return pd.DataFrame(normalize(pd.DataFrame(self.nmf.fit_transform(self.data))))
    
    def reduce_labeled(self, labeled_data):
        return pd.DataFrame(normalize(pd.DataFrame(self.nmf.transform(labeled_data))))
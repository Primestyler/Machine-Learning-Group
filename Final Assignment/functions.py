import librosa
import pandas
import numpy
import matplotlib.pyplot as plt
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed

class DataLoader:
    def get_data(self, file_list: list, path: str, max_workers: int = 6) -> pandas.DataFrame:
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
                dataframes[file] = numpy.pad(data, (0, max_length - len(data)), constant_values=numpy.nan)
                
        return pandas.DataFrame(dataframes)
    
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
    
class Visualizer:
    def __init__(self, data: pandas.DataFrame, title: str, rows: int, cols: int, figsize: tuple = (20, 20)):
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
        
        if not isinstance(data, pandas.DataFrame):
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
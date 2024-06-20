import os
import pandas as pd

# Directorio de los archivos CSV procesados por emoción
input_folder = r'C:\Users\Sarah\OneDrive\Documents\EEGModelTrain\EEG_AURA_RFClassification\CSV\csv-fft\fft_emotions\fft_conc_emotions'

# Directorio para guardar el archivo procesado final
output_file = r'C:\Users\Sarah\OneDrive\Documents\EEGModelTrain\EEG_AURA_RFClassification\CSV\csv-fft\fft_concatenated.csv'

# Mapeo de labels a valores numéricos
label_mapping = {
    'neutral': 0.0,
    'happy': 1.0,
    'sad': 2.0,
    'angry': 3.0,
    'disgust': 4.0
}

# Lista de emociones para procesar
emotions = ['happy', 'neutral', 'sad', 'angry', 'disgust']

# Encontrar el archivo con el menor número de filas
min_rows = float('inf')
for emotion in emotions:
    file_path = os.path.join(input_folder, f'{emotion}_concatenated.csv')
    df = pd.read_csv(file_path)
    
    # Eliminar la columna de timestamp si existe
    if 'timestamp' in df.columns:
        df = df.drop(columns=['timestamp'])
    
    num_rows = len(df)
    if num_rows < min_rows:
        min_rows = num_rows

# Recortar los archivos CSV al número mínimo de filas y aplicar el mapeo de labels
concatenated_df = pd.DataFrame()
for emotion in emotions:
    file_path = os.path.join(input_folder, f'{emotion}_concatenated.csv')
    df = pd.read_csv(file_path)
    
    # Eliminar la columna de timestamp si existe
    if 'timestamp' in df.columns:
        df = df.drop(columns=['timestamp'])
    
    df = df.head(min_rows)  # Recortar al número mínimo de filas
    df.iloc[:, -1] = df.iloc[:, -1].map(label_mapping)  # Aplicar el mapeo de labels
    concatenated_df = pd.concat([concatenated_df, df], ignore_index=True)

# Guardar el archivo CSV procesado final
concatenated_df.to_csv(output_file, index=False)
print(f"Archivo CSV procesado generado: {output_file}")

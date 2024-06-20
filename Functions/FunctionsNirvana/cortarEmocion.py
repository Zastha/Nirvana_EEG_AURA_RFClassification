import os
import pandas as pd

# Directorio de los archivos CSV
folder_path = r'C:\Users\Sarah\OneDrive\Documents\EEGModelTrain\EEG_AURA_RFClassification\CSV\csv-fft'

# Crear una nueva carpeta para guardar los archivos filtrados
output_folder = os.path.join(folder_path, 'fft_emotions')
os.makedirs(output_folder, exist_ok=True)

# Lista de emociones para filtrar
emotions = ['happy', 'neutral', 'sad', 'angry', 'disgust']

# Función para filtrar y guardar CSV
def filter_and_save_csv(file_path, emotion, output_folder):
    df = pd.read_csv(file_path)
    
    # Filtrar filas que contienen la emoción especificada
    emotion_df = df[df.iloc[:, -1].str.contains(emotion, case=False, na=False)]
    
    if not emotion_df.empty:
        # Crear el nombre del archivo de salida
        base_name = os.path.basename(file_path)
        output_file = os.path.join(output_folder, os.path.splitext(base_name)[0] + f'_{emotion}.csv')
        
        # Guardar el archivo filtrado
        emotion_df.to_csv(output_file, index=False)
        print(f"Archivo CSV generado: {output_file}")

# Recorrer todos los archivos CSV en el directorio
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

for file in csv_files:
    file_path = os.path.join(folder_path, file)
    
    for emotion in emotions:
        filter_and_save_csv(file_path, emotion, output_folder)

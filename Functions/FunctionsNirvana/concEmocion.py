import os
import pandas as pd

# Directorio de los archivos CSV procesados por emoción
input_folder = r'C:\Users\Sarah\OneDrive\Documents\EEGModelTrain\EEG_AURA_RFClassification\CSV\csv-fft\fft_emotions'

# Crear una nueva carpeta para guardar los archivos concatenados
output_folder = os.path.join(input_folder, 'fft_conc_emotions')
os.makedirs(output_folder, exist_ok=True)

# Lista de emociones para concatenar
emotions = ['happy', 'neutral', 'sad', 'angry', 'disgust']

# Función para concatenar archivos CSV por emoción
def concatenate_csv_by_emotion(emotion, input_folder, output_folder):
    emotion_files = [file for file in os.listdir(input_folder) if file.endswith(f'_{emotion}.csv')]
    
    if emotion_files:
        concatenated_df = pd.DataFrame()
        
        for file in emotion_files:
            file_path = os.path.join(input_folder, file)
            df = pd.read_csv(file_path)
            concatenated_df = pd.concat([concatenated_df, df], ignore_index=True)
        
        # Crear el nombre del archivo de salida
        output_file = os.path.join(output_folder, f'{emotion}_concatenated.csv')
        
        # Guardar el archivo concatenado
        concatenated_df.to_csv(output_file, index=False)
        print(f"Archivo CSV concatenado generado: {output_file}")

# Concatenar archivos para cada emoción
for emotion in emotions:
    concatenate_csv_by_emotion(emotion, input_folder, output_folder)

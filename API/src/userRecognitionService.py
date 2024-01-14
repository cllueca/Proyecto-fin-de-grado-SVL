from joblib import load
import numpy as np 
import random
import tensorflow as tf
import tensorflow.keras as keras
import librosa
from sklearn.preprocessing import StandardScaler

class _User_Recognition_Service_class: # clase singleton, solo se puede crear una instancia

    model = None
    mappings = [False, True]#["No", "Si"]
    scaler = load("keras_utils/scaler22.joblib")
    _instance = None

    def predict(self, audioBBDD, audioNuevo):
        sumaPred = 0

        mfccBBDD = self.preprocess(self, audioBBDD)
        mfccNuevo = self.preprocess(self, audioNuevo)
        
        sumaI = 0
        for i in range(len(mfccBBDD)):
            sumaPred = 0
            for j in range(3):
                rnd = random.randint(0, len(mfccNuevo)-1)
                entrada = [mfccBBDD[i], mfccNuevo[rnd]]
                entrada = np.asarray(entrada).astype('float32')
                entrada = entrada[np.newaxis, ...]
                entrada = self.scaler.transform(entrada.reshape(-1, 11*40)).reshape(-1, 2, 40, 11)
                prediction = self.model.predict(entrada, verbose=False)
                sumaPred+=prediction[0][np.argmax(prediction)]
            sumaPred = sumaPred/3
            print(sumaPred, end=", ")
            sumaI += sumaPred

        media = round(sumaI/len(mfccBBDD), 3)*100
        print(" MEDIA: ", media, "%")
        return media


    def preprocess(self, audioRaw):
        medioSeg = 11025
        
        audio, sr= librosa.load(audioRaw)

        #audio = audio[medioSeg:]
        audio, _ = librosa.effects.trim(audio)

        trozos = self.partirAudio(audio, int(medioSeg/2), int(22050/10)) # audio, ventana de 25ms, espaciado de 10ms
        caracteristicas = []

        for t in trozos:
            caracteristicas.append(np.concatenate((self.obtenerZCR(t), self.obtenerMFCC(t).T), axis=0))

        return np.asarray(caracteristicas).astype('float32')

    def partirAudio(signal, longitudPartes, window_length):
        partes = []
        inicio = 0
        fin = longitudPartes
        while(fin<len(signal)):
            partes.append(signal[inicio:fin])
            inicio = fin-window_length
            fin = fin+longitudPartes-window_length
        
        if len(signal)-inicio > longitudPartes/2:
            partes.append(signal[len(signal)-longitudPartes-window_length:len(signal)-window_length])

        return partes
    
    def obtenerMFCC(trozo):
        mfccs = librosa.feature.mfcc(y=trozo, n_mfcc=13, hop_length=512, n_fft=2048)
                        
        delta_mfccs = librosa.feature.delta(mfccs) # obtencion primer delta de los mfcc
        delta2_mfccs = librosa.feature.delta(mfccs, order=2) # obtencion segundo delta
        mfccs_features = np.concatenate((mfccs, delta_mfccs, delta2_mfccs))

        return mfccs_features.T
    
    def obtenerZCR(trozo):
        return librosa.feature.zero_crossing_rate(trozo)


# Funcion que crea la clase User_Recognition_Service
def User_Recognition_Service():
    # Se comprueba si existe ya la clase y si no es asi, se crea una
    if _User_Recognition_Service_class._instance is None:
        _User_Recognition_Service_class._instance = _User_Recognition_Service_class()
        _User_Recognition_Service_class.model = keras.models.load_model("keras_utils/modelo22.h5")

    # Si no, no se hace nada y se devuelve la clase que ya existia
    return _User_Recognition_Service_class
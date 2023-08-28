import speaker_verification_toolkit.tools as svt
import librosa
import numpy
input
data1, sr = librosa.load('voice1.wav', sr=16000, mono=True)
data2, sr = librosa.load('voice2.wav', sr=16000, mono=True)
data3, sr = librosa.load('voice-viktor.wav', sr=16000, mono=True)
data4, sr = librosa.load('voice-antonio.wav', sr=16000, mono=True)
data5, sr = librosa.load('voice-antonio-2.wav', sr=16000, mono=True)
data6, sr = librosa.load('voice-antonio-3.wav', sr=16000, mono=True)
data7, sr = librosa.load('voice-patrick.wav', sr=16000, mono=True)
data8, sr = librosa.load('voice-patrick-2.wav', sr=16000, mono=True)






data1 = svt.rms_silence_filter(data1)
data2 = svt.rms_silence_filter(data2)
data3 = svt.rms_silence_filter(data3)
data4 = svt.rms_silence_filter(data4)
data5 = svt.rms_silence_filter(data5)
data6 = svt.rms_silence_filter(data6)
data7 = svt.rms_silence_filter(data7)
data8 = svt.rms_silence_filter(data8)


data1 = svt.extract_mfcc(data1)
data2 = svt.extract_mfcc(data2)
data3 = svt.extract_mfcc(data3)
data4 = svt.extract_mfcc(data4)
data5 = svt.extract_mfcc(data5)
data6 = svt.extract_mfcc(data6)
data7 = svt.extract_mfcc(data7)
data8 = svt.extract_mfcc(data8)

voice_data_list_Eduardo=["Eduardo", data1, data2]
voice_data_list_Viktor=["Viktor", data3]
voice_data_list_Antonio=["Antonio", data4, data5, data6]
voice_data_list_Patrick=["Patrick", data7, data8]
voice_data_list=[voice_data_list_Eduardo, voice_data_list_Antonio, voice_data_list_Viktor, voice_data_list_Patrick]
distancia=0
menor_dist=float("inf")
nome_menor_dist=""


for i in range(len(voice_data_list)):
    for j in range(len(voice_data_list[i])):
        if j==0:
            print(f"Distancia {voice_data_list[i][j]}:")
        else:
            distancia+=svt.compute_distance(voice_data_list[i][j], data6)
    print(distancia)
    if distancia<menor_dist:
        menor_dist=distancia
        nome_menor_dist=voice_data_list[i][0]
    distancia=0
print(f"A menor distancia é {nome_menor_dist}")



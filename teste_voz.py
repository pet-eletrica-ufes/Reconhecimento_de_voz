
import speaker_verification_toolkit.tools as svt
import librosa
import numpy
def main():

    data1, sr = librosa.load('patrick/voice-patrick-1.wav', sr=16000, mono=True)
    data2, sr = librosa.load('patrick/voice-patrick-2.wav', sr=16000, mono=True)
    data3, sr = librosa.load('patrick/voice-patrick-3.wav', sr=16000, mono=True)
    data4, sr = librosa.load('patrick/voice-patrick-4.wav', sr=16000, mono=True)
    data5, sr = librosa.load('patrick/voice-patrick-5.wav', sr=16000, mono=True)
    data6, sr = librosa.load('patrick/voice-patrick-6.wav', sr=16000, mono=True)
    data7, sr = librosa.load('patrick/voice-patrick-7.wav', sr=16000, mono=True)
    data8, sr = librosa.load('patrick/voice-patrick-8.wav', sr=16000, mono=True)
    data9, sr = librosa.load('patrick/voice-patrick-9.wav', sr=16000, mono=True)
    data10, sr = librosa.load('patrick/voice-patrick-10.wav', sr=16000, mono=True)
    data11, sr = librosa.load('patrick/voice-patrick-11.wav', sr=16000, mono=True)
    data12, sr = librosa.load('patrick/voice-patrick-12.wav', sr=16000, mono=True)
    data13, sr = librosa.load('patrick/voice-patrick-13.wav', sr=16000, mono=True)
    data14, sr = librosa.load('patrick/voice-patrick-14.wav', sr=16000, mono=True)
    data15, sr = librosa.load('patrick/voice-patrick-15.wav', sr=16000, mono=True)
   


    data1 = svt.rms_silence_filter(data1)
    data2 = svt.rms_silence_filter(data2)
    data3 = svt.rms_silence_filter(data3)
    data4 = svt.rms_silence_filter(data4)
    data5 = svt.rms_silence_filter(data5)
    data6 = svt.rms_silence_filter(data6)
    data7 = svt.rms_silence_filter(data7)
    data8 = svt.rms_silence_filter(data8)
    data9 = svt.rms_silence_filter(data9)
    data10 = svt.rms_silence_filter(data10)
    data11 = svt.rms_silence_filter(data11)
    data12 = svt.rms_silence_filter(data12)
    data13 = svt.rms_silence_filter(data13)
    data14 = svt.rms_silence_filter(data14)
    data15 = svt.rms_silence_filter(data15)


    data1 = svt.extract_mfcc(data1)
    data2 = svt.extract_mfcc(data2)
    data3 = svt.extract_mfcc(data3)
    data4 = svt.extract_mfcc(data4)
    data5 = svt.extract_mfcc(data5)
    data6 = svt.extract_mfcc(data6)
    data7 = svt.extract_mfcc(data7)
    data8 = svt.extract_mfcc(data8)
    data9 = svt.extract_mfcc(data9)
    data10 = svt.extract_mfcc(data10)
    data11 = svt.extract_mfcc(data11)
    data12 = svt.extract_mfcc(data12)
    data13 = svt.extract_mfcc(data13)
    data14 = svt.extract_mfcc(data14)
    data15 = svt.extract_mfcc(data15)

    
    voice_data_list_Viktor=["Viktor"]
    voice_data_list_Antonio=["Antonio"]
    voice_data_list_Patrick=["Patrick", data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15]
    voice_data_list_bandeira=["Bandeira"]
    voice_data_list_Betim=["Betim"]
    voice_data_list_Luca=["Luca"]
    voice_data_list=[voice_data_list_Antonio, voice_data_list_Viktor, voice_data_list_Patrick, voice_data_list_Betim, voice_data_list_bandeira, voice_data_list_Luca]



    distancia=0
    menor_dist=float("inf")
    nome_menor_dist=""


    for i in range(len(voice_data_list)):
        for j in range(len(voice_data_list[i])):
            if j==0:
                print(f"Distancia {voice_data_list[i][j]}:")
            else:
                distancia+=svt.compute_distance(voice_data_list[i][j], data8)
        distancia=distancia/(len(voice_data_list[i])-1)
        print(distancia)
        if distancia<menor_dist:
            menor_dist=distancia
            nome_menor_dist=voice_data_list[i][0]
        distancia=0
    print(f"A menor distancia é {nome_menor_dist}")
    
if __name__ == "__main__":
    main()



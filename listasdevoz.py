import speaker_verification_toolkit.tools as svt
import librosa
import numpy
from captura_de_voz import captura_voz
from report import write_report




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
data16, sr = librosa.load('antonio/voice-antonio-1.wav', sr=16000, mono=True)
data17, sr = librosa.load('antonio/voice-antonio-2.wav', sr=16000, mono=True)
data18, sr = librosa.load('antonio/voice-antonio-3.wav', sr=16000, mono=True)
data19, sr = librosa.load('antonio/voice-antonio-4.wav', sr=16000, mono=True)
data20, sr = librosa.load('antonio/voice-antonio-5.wav', sr=16000, mono=True)
data21, sr = librosa.load('antonio/voice-antonio-6.wav', sr=16000, mono=True)
data22, sr = librosa.load('antonio/voice-antonio-7.wav', sr=16000, mono=True)
data23, sr = librosa.load('antonio/voice-antonio-8.wav', sr=16000, mono=True)
data24, sr = librosa.load('antonio/voice-antonio-9.wav', sr=16000, mono=True)
data25, sr = librosa.load('antonio/voice-antonio-10.wav', sr=16000, mono=True)
data26, sr = librosa.load('antonio/voice-antonio-11.wav', sr=16000, mono=True)
data27, sr = librosa.load('antonio/voice-antonio-12.wav', sr=16000, mono=True)
data28, sr = librosa.load('antonio/voice-antonio-13.wav', sr=16000, mono=True)
data29, sr = librosa.load('antonio/voice-antonio-14.wav', sr=16000, mono=True)
data30, sr = librosa.load('antonio/voice-antonio-15.wav', sr=16000, mono=True)

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
data16 = svt.rms_silence_filter(data16)
data17 = svt.rms_silence_filter(data17)
data18 = svt.rms_silence_filter(data18)
data19 = svt.rms_silence_filter(data19)
data20 = svt.rms_silence_filter(data20)
data21 = svt.rms_silence_filter(data21)
data22 = svt.rms_silence_filter(data22)
data23 = svt.rms_silence_filter(data23)
data24 = svt.rms_silence_filter(data24)
data25 = svt.rms_silence_filter(data25)
data26 = svt.rms_silence_filter(data26)
data27 = svt.rms_silence_filter(data27)
data28 = svt.rms_silence_filter(data28)
data29 = svt.rms_silence_filter(data29)
data30 = svt.rms_silence_filter(data30)

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
data16 = svt.extract_mfcc(data16)
data17 = svt.extract_mfcc(data17)
data18 = svt.extract_mfcc(data18)
data19 = svt.extract_mfcc(data19)
data20 = svt.extract_mfcc(data20)
data21 = svt.extract_mfcc(data21)
data22 = svt.extract_mfcc(data22)
data23 = svt.extract_mfcc(data23)
data24 = svt.extract_mfcc(data24)
data25 = svt.extract_mfcc(data25)
data26 = svt.extract_mfcc(data26)
data27 = svt.extract_mfcc(data27)
data28 = svt.extract_mfcc(data28)
data29 = svt.extract_mfcc(data29)
data30 = svt.extract_mfcc(data30)




voice_data_list_Viktor=["Viktor"]
voice_data_list_Antonio=["Antonio", data16, data17, data18, data19, data20, data21, data22, data23, data24, data25, data26, data27, data28, data29, data30]
voice_data_list_Patrick=["Patrick", data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15]
voice_data_list_bandeira=["Bandeira"]
voice_data_list_Betim=["Betim"]
voice_data_list_Luca=["Luca"]
voice_data_list=[voice_data_list_Antonio,  voice_data_list_Patrick]
datateste_list=[]



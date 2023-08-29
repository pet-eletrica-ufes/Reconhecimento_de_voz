import speaker_verification_toolkit.tools as svt
import librosa
import numpy
from captura_de_voz import captura_voz
from report import write_report
from listasdevoz import voice_data_list, datateste_list

def main():
    
    acerto=""
    distancia=0
    menor_dist=float("inf")
    nome_menor_dist=""
    pessoa=input("Diga seu nome: ")
    

    for i in range(3):
        captura_voz(pessoa, 1, i)
        datateste, sr = librosa.load(f'voice-{pessoa}-{i}.wav', sr=16000, mono=True)
        datateste =svt.rms_silence_filter(datateste)
        datateste =svt.extract_mfcc(datateste)
        datateste_list.append(datateste)
       
    for a in range(len(datateste_list)):
        for i in range(len(voice_data_list)):
            for j in range(len(voice_data_list[i])):
                if j==0:
                    print(f"Distancia {voice_data_list[i][j]}:")
                else:
                    distancia+=svt.compute_distance(voice_data_list[i][j], datateste_list[a])
            distancia=distancia/(len(voice_data_list[i])-1)
            print(distancia)
            if distancia<menor_dist:
                menor_dist=distancia
                nome_menor_dist=voice_data_list[i][0]
            distancia=0
        if nome_menor_dist==pessoa:
                acerto="sim"
        else:
                acerto="nao"
        
        write_report(f"report/relatorio{a+1}.txt", pessoa, acerto, nome_menor_dist, menor_dist)

    datateste_list.clear()
    
if __name__ == "__main__":
    main()



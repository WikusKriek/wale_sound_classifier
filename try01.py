import io
import os
import math


wave_file = "./HumpBackWhale_Sounds"
txt_file = "./HumpBackWhale_Times"
sounds = os.listdir(wave_file)
times = os.listdir(txt_file)
whale_sounds_list = []
whale_times_list = []
for sound in sounds:
    whale_sounds_list.append(sound)
for time in times:
    whale_times_list.append(time)
whale_sounds_list = sorted(whale_sounds_list)
whale_times_list = sorted(whale_times_list)

print("sl : ", whale_sounds_list)
print("tl : ", whale_times_list)

start_time_file = []
end_time_file = []
list_lengths = []

k = 0
for index_times in range(0, len(whale_times_list)):
    file = whale_times_list[index_times]
    with io.open(txt_file + "/" + file, mode="r", encoding="utf-8") as f:
        temp = []
        i = 0
        start_time_file = []
        end_time_file = []
        for line in f:
            temp.append(line.split())
            start_time_file.append(float(temp[i][0]))
            end_time_file.append(float(temp[i][1]))
            i += 1
        list_lengths.append(i)



print("List_Lengths: ", list_lengths)
print("List_Length: ", len(list_lengths))
print("Length Audio file: ", len(whale_sounds_list))
print(start_time_file)
print(end_time_file)


sound_duration = [] 

print(sound_duration)
i = 0
sound_duration = [902, 865, 530, 165, 124, 189, 251, 906, 909, 905, 908, 255]
outout = [None] * 255
i = 0
for k in range(255):
    if ((start_time_file[i]-k)>1):
        val=1
    elif (k>end_time_file[i]and k+1<start_time_file[i+1]):
        val=0
        i+=1
    elif (k<start_time_file[i]):
        val=1-(start_time_file[i]-k)
    elif(k >start_time_file[i] and k+1 <end_time_file[i]):
        val=1
    elif(k+1 >end_time_file[i] and k+1 <start_time_file[i+1]):
        val=1-(k+1 -end_time_file[i])
        i+=1
    elif(k+1 >end_time_file[i] and k+1 >start_time_file[i+1]):
        val=(end_time_file[i]-k)+(k+1 -start_time_file[i+1])
        i+=1
    

    sound_duration.append(val)
    #print (val)



print(sound_duration)
print(len(sound_duration))
print(max(end_time_file))
import io
import os
import math
import torchaudio


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

start_time = []
end_time = []
sound_duration = []
segment_length = 4000
for i in range(0, len(whale_sounds_list), 1):
    sound_file = wave_file + "/" + whale_sounds_list[i]
    waveform, sample_rate = torchaudio.load(sound_file)
    length_time = math.floor(waveform.shape[1] / segment_length)
    sound_duration.append(length_time)
    start_time1 = 0
    end_time1 = 1
    for j in range(0, sound_duration[i], 1):
        start_time.append(start_time1)
        end_time.append(end_time1)
        start_time1 += 1
        end_time1 += 1
print(start_time)
print(end_time)
print(sound_duration)
counter = 0
for i in range(len(sound_duration)):
    for k in range(sound_duration[i]):
        try:
            for j in range(list_lengths[i]):
                if start_time[k] >= start_time_file[j] and end_time[k] <= end_time_file[j]:
                    print("Number: ", k, "Range: ", start_time[k], "-", end_time[k])
                elif start_time[k] > start_time_file[j]:
                    if ((end_time_file[j] - start_time[k]) / (end_time_file[j] - start_time_file[j])) * 100 >= 0:
                        print("Number: ", k, "Diff: ", ((end_time_file[j] - start_time[k]) / (end_time_file[j] - start_time_file[j])) * 100)
                        counter += 1
                elif start_time[k] < start_time_file[j]:
                    if float(((end_time[k] - start_time_file[j])/(end_time_file[j]-start_time_file[j])) * 100) >= 0:
                        print("Number: ", k, "Diff: ",  ((end_time[k] - start_time_file[j])/(end_time_file[j]-start_time_file[j])) * 100)
                        counter += 1
        except:
            print("Number: ", k)



print(counter)
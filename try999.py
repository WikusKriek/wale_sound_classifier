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
time_len = []
start_time_files = []
end_time_files = []
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
        start_time_files.append(start_time_file)
        end_time_files.append(end_time_file)


print("List_Lengths: ", list_lengths)
print("List_Length: ", len(list_lengths))
print("Length Audio file: ", len(whale_sounds_list))
#print(start_time_file)
#print(end_time_file)

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

print(sound_duration)
#print(start_time)
#print(end_time)

list_timeDiff = []
list_startTimeFractions = []
list_endTimeFractions = []
curStartTime = []
curEndTime = []
for j in range(len(start_time_files)):
    curStartTime = start_time_files[j]
    curEndTime = end_time_files[j]
    time_diff = []
    start_time_fraction = []
    end_time_fraction = []
    for i in range(len(curStartTime)):
        time_diff.append(curEndTime[i] - curStartTime[i])
        b = 1-(curStartTime[i]%1)
        if(b == 1):
            b = 0
        start_time_fraction.append(b/time_diff[i])
        end_time_fraction.append((curEndTime[i]%1)/time_diff[i])
    list_timeDiff.append(time_diff)
    list_startTimeFractions.append(start_time_fraction)
    list_endTimeFractions.append(end_time_fraction)





j = 0
bool_s = False
outputValues = []
outputVal = []

for k in range(len(sound_duration)):
    for i in range(sound_duration[k]):
        try:
            val_s = start_time_files[k][j]
            val_e = end_time_files[k][j]
            val_t = list_timeDiff[k][j]
            #print("s : ",val_s,"    e : ",val_e,"       t  : ",val_t, "       bool : ", bool_s)

            if(bool_s == True):
                if(i+1 < val_e):
                    outputVal.append(1)
                elif(i < val_e):
                    outputVal.append(list_endTimeFractions[k][j])
                    j = j + 1
                    bool_s = False
            else:
                if(float(i) == val_s):
                    outputVal.append(1)
                    bool_s = True
                elif (i + 1 > val_s):
                    if 1 + i > val_e:
                        outputVal.append(1)
                        j += 1
                    else:
                        outputVal.append(list_startTimeFractions[k][j])
                        bool_s = True
                else:
                    outputVal.append(0)
            print(i, " - ", i + 1, " : ", outputVal[i])
        except:
            outputVal.append(0)
    outputValues.append(outputVal)
    j = 0



# k = 0
# for i in range(len(outputValues[k])):
#     print(i," - ",i+1, " : ", outputValues[k][i])

'''
counter = 0
for i in range(0, len(whale_sounds_list), 1):
    for k in range(0, sound_duration[i], 1):
        for j in range(0, list_lengths[i], 1):
            #print("start Time: ", start_time[k], "End Time: ", end_time[k])
            #print("start Time File: ", start_time_file[j], "End Time File: ", end_time_file[j])
            if start_time[k] >= start_time_file[j] and end_time[k] <= end_time_file[j]:
                print("Range: ", start_time[k], "-", end_time[k])
                counter += 1
                break
            if start_time[k] >= start_time_file[j]:
                if end_time[k] >= end_time_file[j]:
                    print("Diff: ", ((end_time_file[j]-start_time[k])/(end_time_file[j]-start_time_file[j])) * 100)
                    counter += 1
                    break
            if start_time[k] <= start_time_file[j]:
                if end_time[k] <= end_time_file[j]:
                    print("Diff: ", ((end_time[k]-start_time_file[j])/(end_time_file[j]-start_time_file[j])) * 100)
                    counter += 1
                    break
print(counter)

'''


'''
start_time_file = 0.99
end_time_file = 2.53

start_time = [0, 1, 2]
end_time = [1, 2, 3]

for i in range(0, 3, 1):
    if start_time[i] >= start_time_file and end_time[i] <= end_time_file:
        print("Range: ", start_time[i], "-", end_time[i])
    elif start_time[i] > start_time_file:
        print("Diff: ", ((end_time_file - start_time[i])/(end_time_file-start_time_file)) * 100)
    elif start_time[i] < start_time_file:
        print("Diff: ",  ((end_time[i] - start_time_file)/(end_time_file-start_time_file)) * 100)
        
        
            elif start_time[k] > start_time_file[j]:
                if ((end_time_file[j] - start_time[k]) / (end_time_file[j] - start_time_file[j])) * 100 >= 0:
                    print("Diff: ", ((end_time_file[j] - start_time[k]) / (end_time_file[j] - start_time_file[j])) * 100)
                    counter += 1
                elif start_time[k] < start_time_file[j]:
                    if ((end_time[k] - start_time_file[j])/(end_time_file[j]-start_time_file[j])) * 100 >= 0:
                        print("Diff: ",  ((end_time[k] - start_time_file[j])/(end_time_file[j]-start_time_file[j])) * 100)
                        counter += 1
                elif start_time[k] < start_time_file[j] and end_time[k] < end_time_file[j]:
                    print("Range 0")
'''
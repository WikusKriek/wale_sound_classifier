import io
import os
import math
import torch

out = []
txt_file = "./HumpBackWhale_Times_test"
times = os.listdir(txt_file)
whale_times_list = []
for time in times:
    whale_times_list.append(time)
whale_times_list = sorted(whale_times_list)

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
        #sound_duration = [903, 866, 385, 166, 125, 190, 252, 910, 906, 909, 256]
        sound_duration = [341]
        outout = []
        outout = [0] * sound_duration[k]
        for i in range(len(start_time_file)):
            end = end_time_file[i]
            start = start_time_file[i]
            n = math.ceil(end) - math.floor(start)  # 1.41
            if (n < 0):
                print("een moerse error die walvis is dooi")
                print(i)
                print(start_time_file[i])
                print(end_time_file[i])
                break

            elif (n == 1):
                outout[math.ceil(end)] += end - start
            else:
                for l in range(n):
                    if (l == 0):
                        outout[math.ceil(start)] += math.ceil(start) - start
                    elif (l == n - 1):
                        outout[math.ceil(end)] += end - math.floor(end)
                    else:
                        outout[math.ceil(start) + l] = 1

                list_lengths.append(i)

        output = outout.pop(0)
        out = out + outout
        k += 1

print(out)
out.pop(1246)
print(len(out))
print(sum(sound_duration) - 1)

PATH1 = './Model/TestSet_Labels_New.pt'
torch.save(out, PATH1)
out = torch.load(PATH1)
print('Model Loaded')

print(out)
print(len(out))

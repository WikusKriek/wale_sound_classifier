import io
import os


txt_file = "./HumpBackWhale_Times"
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
        for line in f:
            temp.append(line.split())
            start_time_file.append(float(temp[i][0]))
            end_time_file.append(float(temp[i][1]))
            i += 1
        list_lengths.append(i)


print("List_Lengths: ", list_lengths)
print("List_Length: ", len(list_lengths))
print(start_time_file)
print(end_time_file)
print("List_Lengths: ", list_lengths)
print("List_Length: ", len(list_lengths))

sound_duration = [902, 865, 530, 165, 124, 189, 251, 906, 909, 905, 908, 255]
outout = [None] * 50000
i = 0
for dur in range(len(sound_duration)):
    for k in range(sound_duration[dur]):

        if ((start_time_file[i]-k)>1):
            val=0
        elif (k<start_time_file[i]):
            val=1-(start_time_file[i]-k)
        elif(k >=start_time_file[i] and k+1 <=end_time_file[i]):
            val=1
        elif(k+1 >end_time_file[i] and k+1 <start_time_file[i+1]):
            val=1-(k+1 -end_time_file[i])
            i+=1
        elif(k+1 >end_time_file[i] and k+1 >start_time_file[i+1]):
            val=(end_time_file[i]-k)+(k+1 -start_time_file[i+1])
            i+=1
        else:
            val = 0


        outout[i]=val
        #print ("i: ", k, "Value: ", val)

print(start_time_file)
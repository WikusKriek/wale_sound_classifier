import io
import os
import math


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
        start_time_file = []
        end_time_file = []
        for line in f:
            temp.append(line.split())
            start_time_file.append(float(temp[i][0]))
            end_time_file.append(float(temp[i][1]))
            i += 1
        sound_duration = [903, 866, 531, 166, 125, 190, 252, 907, 910, 906, 909, 256]
        outout = [0] * sound_duration[k]
        for i in range(len(start_time_file)):
            end = end_time_file[i]
            start = start_time_file[i]
            n = math.ceil(end)-math.floor(start)  # 1.41
            if(n<0):
                print ("een moerse error die walvis is dooi")
                print(i)
                print(start_time_file[i])
                print(end_time_file[i])
                break
            
            elif(n==1): 
                outout[math.ceil(end)] += end-start
            else :
                for l in range(n):
                    if(l==0):
                        outout[math.ceil(start)] +=math.ceil(start)- start
                        print(start-math.ceil(start))
                    elif(l==n-1):
                        outout[math.ceil(end)] += end -math.floor(end)
                        print(end -math.floor(end))
                    else:
                        outout[math.ceil(start)+l] =1
                        print(1)
                list_lengths.append(i)
        print(outout)
        k+=1


print("List_Lengths: ", list_lengths)
print("List_Length: ", len(list_lengths))
print(start_time_file)
print(end_time_file)
print("List_Lengths: ", list_lengths)
print("List_Length: ", len(list_lengths))

sound_duration = [902, 865, 530, 165, 124, 189, 251, 906, 909, 905, 908, 255]
outout = [0] * sum(sound_duration)
k>end_time_file[i]and k+1<start_time_file[i+1]


for i in range(len(start_time_file)):
    end = end_time_file[i]
    start = start_time_file[i]
    n = math.ceil(end)-math.floor(start)  # 1.41
    if(n<0):
        print ("een moerse error die walvis is dooi")
        print(i)
        print(start_time_file[i])
        print(end_time_file[i])
        break
    
    elif(n==1): 
        outout[math.ceil(end)] += end-start
    else :
        for l in range(n):
            if(l==0):
                outout[math.ceil(start)] +=math.ceil(start)- start
                print(start-math.ceil(start))
            elif(l==n-1):
                outout[math.ceil(end)] += end -math.floor(end)
                print(end -math.floor(end))
            else:
                outout[math.ceil(start)+l] =1
                print(1)
        
   

    
    #print (val)



print(outout)

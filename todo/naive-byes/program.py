import csv

data=[]

with open(r"C:\Users\sahuj\Desktop\python\todo\naive-byes\data.csv", 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
   
    for row in csv_reader:
        data.append(row)
       
def probability(data, num, insta):
    count = 0
    for datas in data:
        if datas[num].strip() == insta.strip():
            count += 1
    return count / len(data)

def get_new_instance():
    new_instance=[]
    for i in range(4):
        new_instance.append(input())
    return new_instance
new_instance = get_new_instance()

def get_probability(data,val):
    data1=[]
    data2=[]
    yes_p={}
    no_p={}
    for datas in data:
        if datas[4].strip() == 'yes':
            data1.append(datas)
        else:
            data2.append(datas)

    yes_p['sunny']=probability(data1,0,'sunny')
    yes_p['rainy']=probability(data1,0,'rainy')
    yes_p['overcast']=probability(data1,0,'overcast')
    yes_p['hot']=probability(data1,1,'hot')
    yes_p['mild']=probability(data1,1,'mild')
    yes_p['cold']=probability(data1,1,'cold')
    yes_p['high']=probability(data1,2,'high')
    yes_p['normal']=probability(data1,2,'normal')
    yes_p['true']=probability(data1,3,'true')
    yes_p['false']=probability(data1,3,'false')
    
    no_p['sunny']=probability(data2,0,'sunny')
    no_p['rainy']=probability(data2,0,'rainy')
    no_p['overcast']=probability(data2,0,'overcast')
    no_p['hot']=probability(data2,1,'hot')
    no_p['mild']=probability(data2,1,'mild')
    no_p['cold']=probability(data2,1,'cold')
    no_p['high']=probability(data2,2,'high')
    no_p['normal']=probability(data2,2,'normal')
    no_p['true']=probability(data2,3,'true')
    no_p['false']=probability(data2,3,'false')
    
    if val =='yes':
        return yes_p
    else:
        return no_p
      
def naive_byes(new_instance):
    yes_prob = probability(data, 4, 'yes')
    no_prob = probability(data, 4, 'no')
    
    yes_p = get_probability(data,'yes')
    no_p = get_probability(data,'no')

    prob_yes = yes_prob *(yes_p[new_instance[0]]) *(yes_p[new_instance[1]]) *(yes_p[new_instance[2]]) * (yes_p[new_instance[3]])
    prob_no = no_prob *(no_p[new_instance[0]]) *(no_p[new_instance[1]]) *(no_p[new_instance[2]]) * (no_p[new_instance[3]])
    
    print(prob_yes)
    print(prob_no)

    if prob_yes > prob_no:
        print("Tennis game will be played")
    else:
        print("No tennis game will be played")

naive_byes(new_instance)

   
       
               

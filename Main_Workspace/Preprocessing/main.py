import json
import datetime
data=[]
with open('./Main_Workspace/data/jsondata.json') as f:
    data=json.load(f)
# print(data)
# print(data.keys())
i=0
for key,value in data.items():
    print(key)
    year=int(key[0:4])
    month=int(key[5:7])
    day=int(key[8:10])
    date=datetime.date(year,month,day)
    ordinaldate=datetime.datetime.toordinal(date)
    print(date)
    print(ordinaldate)

    total_confirmed=0
    total_recovered=0
    total_deaths=0
    tota_tested=0
    total_active=0

    delta_confirmed=0
    delta_recovered=0
    delta_deaths=0
    delta_tested=0
    delta_active=0

    delta7_confirmed=0
    delta7_recovered=0
    delta7_deaths=0
    delta7_tested=0
    delta7_active=0

    total_other=0
    delta_other=0
    delta7_other=0





    # print(value['MH'])



    try:
        print(value['TT'])
        if value['TT']!=None:
            try:
                if value['TT']['delta']!=None:
                    # print(value['TT']['delta'])
                    try:
                        print("Confirmed in delta : ",value['TT']['delta']['confirmed'])
                        delta_confirmed=value['TT']['delta']['confirmed']
                    except:
                        pass
                    try:
                        print("Confirmed in delta : ",value['TT']['delta']['recovered'])
                        delta_recovered=value['TT']['delta']['recovered']
                        

                    except:
                        pass
                    try:
                        print("Confirmed in delta : ",value['TT']['delta']['deceased'])
                        delta_deaths=value['TT']['delta']['deceased']
                        

                    except:
                        pass
                    try:
                        print("Confirmed in delta : ",value['TT']['delta']['tested'])
                        delta_tested=value['TT']['delta']['tested']
                        

                    except:
                        pass
                    try:
                        print("Confirmed in delta : ",value['TT']['delta']['other'])
                        delta_other=value['TT']['delta']['other']
                        
                    except:
                        pass
                    delta_active=delta_confirmed-delta_recovered-delta_deaths-delta_other
                    print("delta active : ",delta_active)

                pass
            except:
                pass
            try:
                if value['TT']['delta7']!=None:
                    # print(value['TT']['delta7'])
                    try:
                        pass

                    except:
                        pass
                    try:
                        pass

                    except:
                        pass
                    try:
                        pass

                    except:
                        pass
                    try:
                        pass

                    except:
                        pass
                    try:
                        pass

                    except:
                        pass



                pass
            except:
                pass
            try:
                if value['TT']['total']!=None:
                    # print(value['TT']['total'])
                    try:
                        pass

                    except:
                        pass
                    try:
                        pass

                    except:
                        pass
                    try:
                        pass

                    except:
                        pass
                    try:
                        pass

                    except:
                        pass
                    try:
                        pass

                    except:
                        pass



                pass
            except:
                pass


            pass
        
        print("try")
    except:
        continue


    i+=1
    if(i==10):
        break


import subprocess
import re 

    command_output=subprocess.run(["netsh","wlan", "show","profiles"],capture_output=True).stdout.decode() 

    profil_name= re.findall("All User Profile   : (.*)\r", command_output)

    wifi_list=[]
    wifi_list[0].encode('ascii','ignore').decode()
    command_output[0].encode('ascii','ignore').decode()

    if len(profil_name) !=0: 
        for name in profil_name:
            wifi_profile={} 

            profile_info=subprocess.run(["netsh","wlan","show","profile",name],capture_output=True,shell=True).stdout.decode() 

            if re.search("Security key     : Absent",profile_info): 
                continue
            else:
                wifi_profile["ssid"]=name
                profile_info_pass=subprocess.run(["netsh","wlan","show","profile",name,"key=clear"],capture_output=True).stdout.decode()   


                password=re.search("Key Content     : (.*)\r",profile_info_pass)

                if password == None:
                    wifi_profile["password"]= None
                else:
                    wifi_profile["password"]=password[1]
                wifi_list.append(wifi_profile)

    for x in range(len(wifi_list)):
        print(wifi_list[x])

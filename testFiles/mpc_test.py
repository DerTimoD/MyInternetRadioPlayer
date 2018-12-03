#%%
import subprocess

#%% Play Number
number = 7
output =  subprocess.check_output(['mpc', 'play', str(number)])
print(output)

#%% Toggle 
number = 1
output =  subprocess.check_output(['mpc', 'toggle'])
print(output)

#%% Pause
number = 8
output =  subprocess.check_output(['mpc', 'pause'])
print(output)


#%% Stopp
output =  subprocess.check_output(['mpc', 'stop'])
print(output)

#%% Playlist
output =  subprocess.check_output(['mpc', 'playlist'])
print(output)
stringOut = str(output).split("\n")
print(stringOut)


#%% Current
output =  subprocess.check_output(['mpc', 'current'])
#print(output)
stringOut = str(output).split(":")
station = stringOut[0].strip('b\"')
stringOut = stringOut[1].split('-')
artist = stringOut[0]
song = stringOut[1].strip(" \\n")

print("Station:\t" + station)
print("Artist:\t" + artist)
print("Song:\t" + song)

#%% MPD Stats
output =  subprocess.check_output(['mpc', 'stats'])
print(output)


#%% MPC
output =  subprocess.check_output(['mpc'])
stringOut = str(output).split("\\n")
for i in range(len(stringOut)):
    print(stringOut[i])

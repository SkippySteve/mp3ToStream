import sys		#for args and ending if not enough args supplied
import os		#for getting list of files in mp3 directory
import subprocess	#for issuing ffmpeg commands
import random		#for randomness of shuffle

if len(sys.argv) < 4:
	print("Less than needed number of arguments provided. Example: python livestream.py mp3.Directory.Here ImageHere StreamKeyHere")
	sys.exit()


dir_list = os.listdir(sys.argv[1])
mp3List = []

print("Input dir for mp3s: ", sys.argv[1])
print("Image to use: ", sys.argv[2])

for file in dir_list:
	if file[-4:] == ".mp3":
		mp3List.append(file)

print("Found ", len(mp3List), " mp3s in provided dir")

numNotOne = 0

while numNotOne != 1:	#just ensuring the loop never ends...
	currentTrack = mp3List[random.randrange(len(mp3List))]
	print("Currently playing: ", currentTrack)
	subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-re", "-loop", "1", "-f", "image2", "-i", sys.argv[2], "-i", str(sys.argv[1]+currentTrack), "-codec:a", "copy", "-shortest", "-f", "flv", sys.argv[3])])

#for text on screen, arg for ffmpeg: "-vf", str("drawtext=fontfile=/usr/share/fonts/FiraSans-Heavy.ttf:text="+currentTrack+":fontcolor=white:fontsize=24:box=1:boxcolor=black@0.5:boxborderw=5:x=(w-text_w)/2:y=(h-text_h)/4)"

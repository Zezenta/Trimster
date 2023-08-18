import math
import re
from moviepy.video.io.VideoFileClip import VideoFileClip

print("Made with love by Zezenta") #;)
filename = input("Please enter the name of the file that you would like to trim: ") #example: testvid.mp4
pattern = r'([\w\s\_\-]+)\.\w+' #This regex indicates any kind of alphanumerical number, and "-" or "_" characters, one time or more. Then, a single period. And finally, captures any alphanumerical text (hence, the extension)
video_groups = re.match(pattern, filename)
video_name = video_groups.group(1)

def get_video_duration(fileToCheck):
    try:
        videoToCheck = VideoFileClip(fileToCheck) #We atribute the file to the videoToCheck variable
        duration = videoToCheck.duration #We pull the duration
        videoToCheck.close()  # Close the video clip
        return duration #We return the duration value (in seconds)
    except Exception as e:
        print(f"Error: {e}") #If there is an error, we specify what it is
        return None
    
file_duration = get_video_duration(filename) #We execute the function

rounded_num_segments = math.floor(file_duration / 30)
leftover_time_decimal = file_duration - (rounded_num_segments * 30)
leftover_time = round(leftover_time_decimal, 2)

for i in range(rounded_num_segments):
   print(f'Creating "{video_name} Part {i+1}.mp4"')
   video_clip = VideoFileClip(filename)
   start_time = i * 30
   end_time = (i + 1) * 30
   trimmed_clip = video_clip.subclip(start_time, end_time)
   trimmed_clip.write_videofile(f"{video_name} Part {i+1}.mp4")
   video_clip.close()

if leftover_time > 0:
    print(f'Creating "{video_name} Part {rounded_num_segments + 1}.mp4"')
    video_clip = VideoFileClip(filename)
    trimmed_clip = video_clip.subclip((rounded_num_segments * 30), file_duration)
    final_part = rounded_num_segments + 1
    trimmed_clip.write_videofile(f"{video_name} Part {final_part}.mp4")
    video_clip.close()

print("All videos have been created!")
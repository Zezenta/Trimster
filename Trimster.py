from moviepy.video.io.VideoFileClip import VideoFileClip

print("Made with love by Zezenta") #;)
filename = input("Please enter the name of the file that you would like to trim") #example: testvid.mp4
num_segments = int

def get_video_duration(fileToCheck):
    try:
        video_clip = VideoFileClip(fileToCheck) #We atribute the file to the video_clip variable
        duration = video_clip.duration #We pull the duration
        video_clip.close()  # Close the video clip
        return duration #We return the duration value (in seconds)
    except Exception as e:
        print(f"Error: {e}") #If there is an error, we specify what it is
        return None
    
file_duration = get_video_duration(filename) #We execute the function

print(file_duration) #We print the duration
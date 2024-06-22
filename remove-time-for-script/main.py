
import os
import re

current_file_path = os.path.abspath(__file__)
current_dirname = os.path.dirname(current_file_path)
target_file_path = os.path.join(current_dirname, "youtube_transcript.txt")
new_target_file_path = os.path.join(current_dirname, "new_youtube_transcript.txt")

pattern = r'\d{2}:\d{2}:\d{2}\.\d{3}\s+'

with open(target_file_path) as file:
    lines = file.readlines()

with open(new_target_file_path, "w") as new_file:
    for line in lines:
        new_line = re.sub(pattern, '', line)
        
        new_file.write(new_line)
        
        
    
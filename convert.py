import json
import os

from moviepy.audio.io.AudioFileClip import AudioFileClip

# dirt store output file
dirt_path = 'J:/video2audio/ost/'


# convert Bili Bili video to audio
def convert(file):
    file_list = os.walk(file)
    for f in file_list:
        # [0] path, [1]] child folder list, [2] file list
        path = f[0] + '\\'  # dict path
        # if there are files
        if f[2]:
            # print(f[2])
            # find out entry.json, get title
            for child_file in f[2]:
                if os.path.basename(child_file) == 'entry.json':
                    with open(path + child_file, 'r', encoding='utf-8') as json_str:
                        data = json_str.read()
                        title = get_name(data, 'page_data')
                        print('file name --- ' + title)
                # find out video, convert it
                elif os.path.basename(child_file) == '0.blv':
                    print('video --- ' + child_file)
                    print(dirt_path + title + ".mp3")
                    print(path + child_file)
                    audio_clip = AudioFileClip(path + child_file)
                    audio_clip.write_audiofile(dirt_path + title + ".mp3")

        else:
            print(path + ' root folder')


# get video title
def get_name(string, key):
    value = ''
    # if type of string is str, transfer to dict
    if isinstance(string, str):
        json_str = json.loads(string)
    # or do nothing, if it is str
    else:
        json_str = string
    for k in json_str:
        if k == key:
            value = json_str[k]
            # if there is 'part'(the title), run again
            if 'part' in value:
                value = get_name(value, 'part')
    return value


if __name__ == '__main__':
    convert('J:/video2audio/17853896')

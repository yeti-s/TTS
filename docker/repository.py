#@title Clone Github Repository
import os

file_path = f"/content/Retrieval-based-Voice-Conversion-WebUI/infer-web.py"
temp_file_path = "/tmp/temp_file.py"
changes_made = False
with open(file_path, "r") as file, open(temp_file_path, "w") as temp_file:
    previous_line = ""
    for line in file:
        new_line = line.replace("value=160", "value=128")
        if new_line != line:
            print("Replaced 'value=160' with 'value=128'")
            changes_made = True
        line = new_line

        new_line = line.replace("crepe hop length: 160", "crepe hop length: 128")
        if new_line != line:
            print("Replaced 'crepe hop length: 160' with 'crepe hop length: 128'")
            changes_made = True
        line = new_line

        new_line = line.replace("value=0.88", "value=0.75")
        if new_line != line:
            print("Replaced 'value=0.88' with 'value=0.75'")
            changes_made = True
        line = new_line

        if "label=i18n(\"输入源音量包络替换输出音量包络融合比例，越靠近1越使用输出包络\")" in previous_line and "value=1," in line:
            new_line = line.replace("value=1,", "value=0.25,")
            if new_line != line:
                print("Replaced 'value=1,' with 'value=0.25,' based on the condition")
                changes_made = True
            line = new_line

        if 'choices=["pm", "harvest", "dio", "crepe", "crepe-tiny", "mangio-crepe", "mangio-crepe-tiny"], # Fork Feature. Add Crepe-Tiny' in previous_line:
            if 'value="pm",' in line:
                new_line = line.replace('value="pm",', 'value="mangio-crepe",')
                if new_line != line:
                    print("Replaced 'value=\"pm\",' with 'value=\"mangio-crepe\",' based on the condition")
                    changes_made = True
                line = new_line

        temp_file.write(line)
        previous_line = line
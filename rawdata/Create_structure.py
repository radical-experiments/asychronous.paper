#!/Users/ozgurkilic/opt/anaconda3/bin/python

import sys
import re
import json

def print_pipelines(pipeline_dict):
    json_str = json.dumps(pipeline_dict, indent=5)
    print(json_str)
    for k,v in pipeline_dict.items():
        for s,t in v.items():
            num_tasks = len(t)
            print("Pipeline:{} Stage:{} NumTasks:{}".format(k,s,num_tasks))


# Define a main function
def main():
    # Check if there is one argument
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        print("Please run the program as follow:\n./Create_structure.py <filename>")
        exit(1)
    # Open the file as f
    with open(filename) as f:
        # Read the file contents line by line
        lines = f.readlines()
    pattern = r"[\" :.;,-]"

    pipeline_dict = {} #9
    #stage_dict = {} #6
    #tasks_list = [] #2

    # Print the lines
    for line in lines:
        allwords = re.split(pattern, line)
        words = list(filter(None, allwords))
#        print(words)
        pipeline = words[9]
        stage = words[6]
        task = words[2]
        if pipeline in pipeline_dict:
            st = pipeline_dict[pipeline]
            if stage in st:
                tl = st[stage]
                if task in tl:
                    continue
                else:
                    tl.append(task)
            else:
                tl = [task]
                st[stage] = tl
        else:
            tl = [task]
            st = {stage:tl}
            pipeline_dict[pipeline]  = st
#        print(line, end="")
    print_pipelines(pipeline_dict)

# Check if the script is executed directly
if __name__ == "__main__":
    # Call the main function
    main()

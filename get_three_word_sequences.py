#!/usr/bin/env python3 

import os
import sys
import re
import time


# This function is to check the validity of the arguments being passed into the script. It returns a dictionary of each argument name and the validated status.
def validate_params(params):
    validated_params = {}
    for i, param in enumerate(params):
        if not os.path.exists(param):            
            validated_params[param] = 1  
        elif not param.endswith('.txt'):            
            validated_params[param] = 2        
        else:
            validated_params[param] = param
    return validated_params


# This function process and prepare the raw text string for the three-word string split. It returns a list of 100 common word sequences in order.
def get_three_word_sequences(raw_text):

    list_of_words = []
    word_dict = {}

    for line in raw_text:                                                   # remove whitespaces and non-alphanumeric characters
        line = line.lower().strip().replace('_', '')                  
        new_line = re.sub('[^\w\s]', '', line)        
        list_of_words.extend(new_line.split())

    curr_seq = ""

    for i in range(len(list_of_words)-2):                                   # iterates the list of words and create a dictionary with three-word strings
        curr_seq = " ".join(list_of_words[i:i+3]) 
        if word_dict.get(curr_seq):
            word_dict[curr_seq] += 1
        else:    
            word_dict[curr_seq] = 1
   

    top_seq = sorted(word_dict, key=word_dict.get, reverse=True)[:100]       # sort the word_dict and only assign the first 100 items to top_seq
    for seq in top_seq:
        print(seq + ' - ', word_dict.get(seq))
    
    return top_seq   


# This function is the main function of the program and it takes in command line arguments and output results depending on the parameters. 
def main(args):
    
    if len(args) == 1 and not sys.stdin.isatty():                            # check if no file is being passed and if so process the sys.stdin
        get_three_word_sequences(sys.stdin)        

    elif len(args) > 1:
        validated_args = validate_params(args[1:])                           # validate arguments
        for v_param, v_status in validated_args.items():
            if v_status == 1:
                print('********** {} does not exist. Please try again. '.format(v_param))
            elif v_status == 2:
                print('********** {} has a file type that is not supported at the moment. '.format(v_param))
            else:                                                            
                with open(v_status, encoding='UTF-8') as raw_text:
                    print('========== Displaying 100 Most Common Three Word Sequences in File: {} '.format(v_param))
                    get_three_word_sequences(raw_text)
                    print('========== END OF WORD FREQUENCES FOR {}'.format(v_param))
    else:
        sys.exit("Program Error: Missing Parameters")

    


if __name__ == "__main__":
    start_time = time.time()
    main(sys.argv)
    print("{} has been used to run this".format(time.time()-start_time))




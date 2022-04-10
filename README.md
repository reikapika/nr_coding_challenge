Get Three Word Sequences
========================

This program is built to return the 100 most common three-word sequences in one or multiple text files. It also takes parameters from non-tty stdin.  
-----------------------------------------------------------------------------------  


# How to Run It #  

* pipe in text content over to the python script using cat command. 
    (e.g. cat moby-dick.txt | python3 get_three_word_sequences.py)

* pass in one or more text file as parameters in command line
    (e.g. python3 moby_dick.txt moby_dick2.txt moby_dick3.txt)

# Bugs #  

* This program may run into errors if sys.stdin arguments being passed is not from a cat command.
* This program may not cover all of the egde text formatting scenarios during the clean up and thus the count may not be accurate in case of over compliex text format. 
* Common edge cases have been tested under limited time and the program may not cover all edge cases. 

# Improvement Plans #  

* This program was developed within a Docker Dev environment and it can be converted over to run using Docker with adding the proper dockerfile and configuration if more research time is given.
* The run time of this program has been tracked with the time module and so far it's performance seems to be alright. However, this has not been tested at scale and should be tested later.

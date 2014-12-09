import subprocess
import time

subprocess.call(['amixer', 'cset', 'numid=3', '1']) #select jack output
subprocess.call(['amixer', 'cset', 'numid=1', '400']) #set volume to maximum 

__popen__ = None

def say(sentence):
    global __popen__

    if __popen__ is not None:
        __popen__.wait()

    print("Saying '{0}'".format(sentence))      
    cmd = ['mpg123', '-q', "http://translate.google.com/translate_tts?tl=en&q={0}".format(sentence)]
    __popen__ = subprocess.Popen(cmd)
    
if __name__ == "__main__":
    say("hello")
    say("supercalifragilisticexpialidocious")
    say("world")

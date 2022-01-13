import glob, os

# Get the list repos for each signal processes
processes = glob.glob("cards/*/")

nSB = 5
for process in processes:
    for SBindex in range(1,nSB+1):
        command = 'python makeCards.py -i {}input_ch{}.txt -o {}ch{}'.format(process, SBindex, process, SBindex)
        print('\n')
        print(command)
        os.system(command)

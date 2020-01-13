import sys
my_input = sys.argv[1]
my_output = sys.argv[2]
inputFile = open(my_input, "r")
outputFile = open(my_output, "w")
read = inputFile.readlines()
my_list = []
for i in read:
    i = i.strip("\n")
    x = i.split("\t")
    my_list.append(x)
new_list = sorted(my_list, key=lambda x : (int(x[0]), int(x[1])))

k = 2
outputFile.write("Message 1\n")
for j in range(len(new_list)):
    outputFile.write("\t".join(new_list[j]))
    outputFile.write("\n")
    try:
        if new_list[j][0] != new_list[j+1][0]:
            outputFile.write("Message {}\n".format(k))
            k += 1
    except IndexError:
        pass
inputFile.close()
outputFile.close()

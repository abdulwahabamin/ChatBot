
import config.py

#First need to seperate out lines and their ids from the rest of the data
def id_to_line(file= movie_lines_file):
	f = open(file).read().split('\n')
	for line in f:
		_line = line.split(' +++$+++ ')
		id_to_line = {}
		if len(_line) == 5:
	            id_to_line[_line[0]] = _line[4]
		# print(id_to_line)
	return id_to_line

#We need to specify the group in which the conversation belong to.
def conv_group(file = conversation_file)
	conv_lines = open(file).read().split('\n')
	convs = [ ]
	for line in conv_lines:
	    _line = line.split(' +++$+++ ')[-1][1:-1].replace("'","").replace(" ","")
	    convs.append(_line.split(','))
	# print(convs)
	return convs

import os

#Change the paths to the files before running this
#-----------------------------------------------------------------------------
base_path = 'D\\Tintash\\'

#-----------------------------------------------------------------------------
# global variables depending on the values in the above module
dataset_folder_name='cornell-movie-dialogs-corpus'
movie_lines_file = os.path.join(base_path, dataset_folder_name, 'movie_lines.txt')
conversation_file = os.path.join(base_path, dataset_folder_name, 'movie_conversation.txt')

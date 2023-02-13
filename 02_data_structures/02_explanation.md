The file structure I'm working with is essentially a tree, and I employed depth-first search to traverse it. Using the os 
module, I determined which items in the current directory are files and added them to a list of files to be returned. Then, I 
recursively walked through the subdirectories within the current directory to find additional files.

The runtime of this approach is O(n * number_of_paths), where n is the total number of files/directories in the path and 
number_of_paths is the number of paths I need to traverse.

The space complexity is O(sibling_nodes * longest_path + num_file_nodes * path_length), where sibling_nodes is the number of 
sibling nodes along the longest path, longest_path is the length of the longest path, num_file_nodes is the number of file 
nodes, and path_length is the length of the path.

import pickle

if __name__ == '__main__':

    with open('banner.p', 'rb') as pickle_file:
        content = pickle.load(pickle_file)
        """
        content is list containing smaller lists (named elements by me)
        each element is made of one or more tuples
        each tuple contains char and num, need to multiply them and join to make a line        
        """

        for element in content:
            print("".join(char * num for char, num in element))

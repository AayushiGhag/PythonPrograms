print("*******WELCOME TO YOUTUBE********")

print("Did you like the video?")





boolean_liked = False
boolean_disliked = False

print("Press 'L' for like and 'D' for dislike the video")

while(True):
    print("Press 'L' for like and 'D' for dislike the video")
    print("if you want to exit, please press 'E'")
    user = input()
    if(user == 'L'):
        if(boolean_liked == False):
            print("You liked the video")
            boolean_liked=True
        else:
            print("You deactivated the liked video")
            boolean_liked= False
    elif(user == 'D'):
        if(boolean_disliked == False):
            print("You disliked the video")
            boolean_disliked=True
        else:
            print("You deactivated the disliked video")
            boolean_disliked=False
    elif(user == 'E'):
        break


print("*******THANK YOUU FOR WATCHING THE VIDEO********")


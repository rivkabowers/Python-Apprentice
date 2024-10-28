"""
Use the words in the list to create a story. 

Use indexing to get words from the list, then 
append them to the story

"""

words = ['Once', '👦', 'upon', '🐕', 'park', 'met', 'with', 'a', 'the', 
    'time', 'to', 'who', '🐈', '👧', 'and', 'went', 'had', 'play', '⚽.', 'they']

story = []

story = story + words[0:1] + words[7:8] + words[1:2] + words[-9:-8] + words[-4:-3]+ words[7:8] + words[3:4] + words[-5:-4] + words[-10:-9] + words[8:9] + words[4:5] + words[6:7] + words[-7:-6] + words[-9:-8] + words[-4:-3]+ words[7:8] + words[-8:-7] + ['.'] + ['there'] + words[19:20] + ['met'] + words[7:8] + words[1:2] + words[-9:-8] + words[-4:-3]+ words[7:8] + words[-8:-7] + words[-6:-5] + words[19:20] + ['played'] + words[6:7] + words[7:8] + words[18:19] + ['together'] + ['.']
#there they met a boy with a cat and they played with a ball together
# Create a story using the words in the list

# Display the story to the user
print(' '.join(story))
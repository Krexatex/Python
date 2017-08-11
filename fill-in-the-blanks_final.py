# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

# sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
# adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
# don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
# tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/
game_data = {
	"easy": {
		"text": '''A common first thing to do in a language is display
'Hello ___1___!'  In ___2___ this is particularly easy; all you have to do
is type in:
___3___ "Hello ___1___!"
Of course, that isn't a very useful thing to do. However, it is an
example of how to output to the user using the ___3___ command, and
produces a program which does something, so it is useful in that capacity.
It may seem a bit odd to do something in a Turing complete language that
can be done even more easily with an ___4___ file in a browser, but it's
a step in learning ___2___ syntax, and that's really its purpose. ''',
		"answers": ["world","Python","print","html"]
	},
	"medium": {
		"text": '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.''',
		"answers": ["function","arguments","None","list"]
	},
	"hard": {
		"text": '''The third major difference between ___1___ and ___2___ is that Python allows you to define many 
'special' ___1___ that are called in unusual ways. All special ___1___ have two underscores before and after their name 
when you define them.
The most important special ___1___ is _____3_____ (short for initialize). This is the ___1___ called when you 
create new ___4___s of a ___5___, so it has to perform any necessary setup. This usually just means initializing any 
___4___ variables (see below) the ___5___ needs. If you don't define an _____3_____ method for your ___5___ Python will insert a 
blank one at runtime (so you'll still be able to create ___4___s of your ___5___, but no variables will be initialized). 
You can define ___3___ to take any number of ___6___, but as usual the first one must be self. For example, the following 
___3___  takes one argument (plus self), and creates two ___4___ variables:
def _____3_____(self, name):
	self.__name = name
	self.__score=0''',
		"answers": ["methods","functions","init","instance","class","arguments"]
	}
}


def difficulty():
	# The difficulty function prompts the user to select the level they'd like to play
	# Then, it runs the corresponding level function defined below
	level = raw_input('''Please select a game difficulty by typing it in! 
Possible choices include easy, medium, and hard.\n''').lower()

	while level not in game_data:
		print ("That's not an option")
		level = raw_input('''\nPlease select a game difficulty by typing it in! 
Possible choices include easy, medium, and hard.\n''').lower()

	output = "\nYou've chosen " + level + "!\n" \
			 "You will get 5 guesses per problem\n" \
			 "The current paragraph reads as such:".format(level)
	print (output)
	answers = game_data[level]["answers"]
	sample = game_data[level]["text"]
	quiz(answers,sample)

def ask_question(sample, string):
	# This is function is used in def quiz to ask the user the answer
	# for the questionnaire 
	print (sample)
	answer = raw_input("\nWhat should be substituted in for " + string + "? ")
	return answer

def quiz (answers, sample):
	"""Play the game Fill in the Blanks
	Args:
    	answers: (list) Answers to the Fill in the Blanks as strings.
    	sample: (str) text with blanks.
    Behavior:
    	User gets a text filled blanks depending on the chosen level
    	and is asked to fill each blank
    Returns:
    	The sample with the blank filled if user answer is correct,
    	or another prompt if incorrect. Up to 5 tries are permitted 
    	per blank space	
	"""
	for text in answers:
		string = "___" + str (answers.index(text)+1) + "___"	
		count = 1
		max_tries = 5
		answer = ask_question(sample, string) 
		while answer.lower() != answers[answers.index(text)].lower():
			if count < 5:
				print ("\nThat isn't the correct answer! Let's try again; you have " + str(max_tries - count) +" attempt(s) left!\n")
				answer = ask_question(sample, string)
			else:
				print ("\nYou've failed too many straight guesses!  Game Over\n")
				return None
			count += 1
		else:
			print (sample.replace(string, answer))
			sample = sample.replace(string, answer)
		continue

difficulty()
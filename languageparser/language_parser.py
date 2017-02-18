# DELPHINUS - ADVENTURE APP
# CS 467 - Winter 2017
# Team Members: Sara Hashem, Shawn Hillyer, Niza Volair
#
# language_parser.py
# Description: Class used to parse the language and return relevant components
# Principal Author of this file per Project plan: Niza Volair
#
# CITATIONS
# CITE: http://docs.python-guide.org/en/latest/intro/learning/
# CITE: https://www.python.org/about/gettingstarted/
# #########################################################################################################


from constants.language_words import *
from languageparser.language_parser_wrapper import *
from fileio.room import *
from fileio.object import *
from debug.debug import *

logger = logging.getLogger(__name__)



class LanguageParser:

	'''
		TODO:

	'''
	def __init__(self):
		logger.debug("Language Parser initialized")


	def parse_command(self, command):
		
		# Go through list of words to parse out words accourding to type and order
		
		#***Valid Structures***
		# VERB
		# VERB->NOUN
		# VERB->PREPOSITION->NOUN
		# VERB->PREPOSITION->NOUN->TARGET
		# VERB->NOUN->PREPOSITION->TARGET
		# NOUN(DIRECTION)
		#**********************
		
		# Note: we are using 'TARGET' to mean 'object of the preposition' to avoid confusion with objects
		
		# TODO: Deal with punctuation accounting for it in messages
		
		# STRETCH GOAL (finished): account for NEGATIONS
		# STRETCH GOAL (finished): account for other word sentence structure
		
		if command == '':
			error = INVALID_EMPTY
			
		command = command.lower().lstrip()

		verb = None
		verb_is_special = False
		noun = None
		noun_is = None
		preposition = None
		target = None
		target_is = None
		error = None
		verb_idx = -1
		prep_idx = -1
		noun_idx = -1
		targ_idx = -1
		last_idx = -1

		# Check for empty string
		if command == '':
			error = INVALID_EMPTY
			
		# parse command into words
		words = command.split()
		
		# VERB check: must have a verb unless we have a destination
		if error == None:
			for idx, word in enumerate(words):
				for alias_array in VERB_ALIASES:
					for verb_alias in alias_array:
						num_words_in_alias = len(verb_alias.split())
						words_sublist = words[idx: (idx + num_words_in_alias)]
						words_sublist_string = ' '.join(words_sublist)
						if words_sublist_string == verb_alias:
							if verb == None:
								# the alias arrays always store the base word at index 0
								verb = str(alias_array[0])
								# index = next word in command we are parsing
								verb_idx = last_idx = idx + num_words_in_alias - 1
							elif idx > last_idx:
								if words_sublist_string == verb:
									error = INVALID_DOUBLE
								else:
									error = INVALID_EXTRA_VERBS
		
		'''
		# TODO: deal with room names
		# Get all of the rooms by name
		self.RoomBuilder = RoomBuilder()
		self.rooms = self.RoomBuilder.load_room_data_from_file("../gamedata/rooms/*.json")
		logger.debug("ROOMS: " + str(self.rooms))
		for room in self.rooms:
			DESTINATION.append(room.get_name())
		'''
		# DESTINATION check: the model is VERB(GO)-> DESTINATION or just a DESTINATION
		if error == None and (verb == None or verb == GO):
			for word in words:
				if word in DESTINATIONS:
					if noun == None:
						verb_is_special = True
						verb = GO
						noun = word
						noun_is ='destination'
					else:
						error = INVALID_EXTRA_DESTINATIONS
		# ERROR check: no verb or destination issue
		if error == None and noun == None and (verb == None or verb == GO):
			if verb == GO:
				error = INVALID_GO_NO_DESTINATION
			else:
				error = INVALID_NO_VERB
	

		# SUBJECT or PREPOSTION check: the model is VERB-> (PREPOSITION ANY SUBSEQUENT LOCATION) + NOUN-> TARGET
		if error == None and verb != GO and noun_is != 'destination':

			# use new var to avoid incorrect list slicing 
			start_idx = last_idx + 1
			
			# for each word in the remaining string, check if noun (object or feature) or preposition
			for idx, word in enumerate(words[start_idx:]):
		
				#PREPOSITION check
				for prep_name in PREPOSITIONS:
					# check number of words in name so we can compare correct number of words from command
					num_words_in_name = len(prep_name.split())
					words_sublist = words[(start_idx + idx): (start_idx + idx + num_words_in_name)]
					words_sublist_string = ' '.join(words_sublist)
					if words_sublist_string == prep_name:
						if preposition == None:
							preposition = words_sublist_string
							prep_idx = last_idx = start_idx + idx + num_words_in_name - 1 
						# currently can only use one
						else:
							error = INVALID_EXTRA_PREPOSITIONS
				#NOUN and TARGET checks
				for obj_alias_array in OBJECT_ALIASES:
					for obj_alias in obj_alias_array:
						# check number of words in alias so we can compare correct number of words from command
						num_words_in_alias = len(obj_alias.split())
						words_sublist = words[(start_idx + idx): (start_idx + idx + num_words_in_alias)]
						words_sublist_string = ' '.join(words_sublist)
						if words_sublist_string == obj_alias:
							# only save  the first occurance of object or feature
							if noun == None:
								# the alias arrays always store the base word at index 0
								noun = str(obj_alias_array[0])
								noun_is = 'object'
								#last index is the last index of the last noun or target we found
								noun_idx = last_idx = start_idx + idx + num_words_in_alias - 1 
							# second occurance will be the target and cannot also be the noun
							elif target == None and noun != str(obj_alias_array[0]):
								target = str(obj_alias_array[0])
								target_is = 'object'
								targ_idx = last_idx = start_idx + idx + num_words_in_alias - 1 
							# current index must > last one we found a noun or target in
							elif start_idx + idx > last_idx:
								if str(obj_alias_array[0]) == noun or str(obj_alias_array[0]) == target:
									error = INVALID_DOUBLE
								else:
									error = INVALID_EXTRA_NOUNS
							# else it is just a double, such as 'floppy disk' which could be 'floppy' and 'disk'
								
				for feat_name_array in FEATURES:
					for feat_name in feat_name_array:
						num_words_in_name = len(feat_name.split())
						words_sublist = words[(start_idx + idx): (start_idx + idx + num_words_in_name)]
						words_sublist_string = ' '.join(words_sublist)
						if words_sublist_string == feat_name:
							if noun == None:
								noun = words_sublist_string
								noun_is = 'feature'
								noun_idx = last_idx = start_idx + idx + num_words_in_name - 1 
							elif target == None and noun != words_sublist_string:
								target = words_sublist_string
								target_is = 'feature'
								targ_idx = last_idx = start_idx + idx + num_words_in_name - 1 
							elif start_idx + idx > last_idx:
								if words_sublist_string == noun or words_sublist_string == target:
									error = INVALID_DOUBLE
								else:
									error = INVALID_EXTRA_NOUNS
		

		#TODO: possibly add TALK to special verbs
		
		#SPECIAL VERB check:
		if error == None:
			#TARGET must be a message string
			if verb == SPRAYPAINT:
				verb_is_special = True
				#VERB(SPRAYPAINT)-TARGET 
				if noun == None:
					if verb_idx + 1 < len(words):
						start_idx = verb_idx + 1
						words_sublist = words[start_idx :]
						target = ' '.join(words_sublist)
						target_is = 'message'
					else:
						error = INVALID_SPRAYPAINT_NO_MESSAGE
				#VERB(SPRAYPAINT)-NOUN-TARGET
				#VERB(SPRAYPAINT)-PREP-NOUN-TARGET
				elif preposition == None or prep_idx < noun_idx:
					if noun_idx + 1 < len(words):
						start_idx = noun_idx + 1
						words_sublist = words[start_idx :]
						target = ' '.join(words_sublist)
						target_is = 'message'
					else:
						error = INVALID_SPRAYPAINT_NO_MESSAGE
			
		#INVALID SENTENCE STRUCTURE check: check for these if not handled by special verbs above:
		if error == None and verb_is_special == False:
			#INVALID: VERB NOUN PREP (no TARGET)
			if noun != None and preposition != None and target == None:
				if prep_idx > noun_idx:
					error = INVALID_SENTENCE_STRUCTURE
			#INVALID: VERB NOUN TARGET PREP
			elif noun != None and target != None and preposition != None:
				if prep_idx > target_idx:
					error = INVALID_SENTENCE_STRUCTURE
			#NEGATION Check: If we have a non special verb sentence, there shouldn't be any negations
			for word in words:
				if word in NEGATIONS:
					error = INVALID_NEGATION

		
		R = LanguageParserWrapper()
		if error != None:
			R.set_error_message(str(error))
			
		if verb != None:
			R.set_verb(str(verb))
		else:
			R.set_verb("")
			
		if noun != None:
			R.set_noun(str(noun), str(noun_is))
		else:
			R.set_noun("", "")
			
		if preposition != None:
			R.set_preposition(str(preposition))
			
		if target != None:
			R.set_extra(str(target), str(target_is))
			
		# logger.debug("Parser returning: \n" + str(R))
		

		return R
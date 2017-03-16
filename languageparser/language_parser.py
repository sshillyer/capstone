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
import string




class LanguageParser:


    def parse_command(self, command):
        
        # Go through list of words to parse out words according to type and order
        
        #***Valid Structures***
        # VERB
        # VERB->NOUN
        # VERB->PREPOSITION->NOUN
        # VERB->PREPOSITION->NOUN->TARGET
        # VERB->NOUN->PREPOSITION->TARGET
        # NOUN(DIRECTION)
        #**********************
        
        # Note: we are using 'TARGET' to mean 'object of the preposition' to avoid confusion with objects
        
        if command == '':
            error = INVALID_EMPTY
            
        #save a copy of original in case we need for spraypaint
        sprayCommand = command
        
        #otherwise capitalization doesn't matter
        command = command.lower().lstrip()

        verb = None
        verb_is_special = False
        noun = None
        noun_is = None
        preposition = None
        target = None
        target_is = None
        error = None
        cheat = None
        verb_idx = -1
        prep_idx = -1
        noun_idx = -1
        targ_idx = -1
        last_idx = -1

        # check for cheat codes    
        for alias in CHEATCODE_LOSE_ALIASES:
            if alias in command:
                verb  = CHEATCODE_LOSE
                cheat = True
        
        for alias in CHEATCODE_WIN_ALIASES:
            if alias in command:
                verb = CHEATCODE_WIN
                cheat = True
                

        # Check for empty string
        if command == '':
            error = INVALID_EMPTY
            
        # DESTINATION check: the model is VERB(GO)-> DESTINATION or just a DESTINATION
        if error == None and cheat == None:
            for dest_alias_array in DESTINATIONS:
                for dest_alias in dest_alias_array:
                    if dest_alias in command:
                        if noun == None:
                            noun = dest_alias_array[0]
                            noun_is ='destination'
                        elif noun != dest_alias_array[0]:
                            error = INVALID_EXTRA_DESTINATIONS
                        
        # parse command into words
        words = command.split()

        # VERB check: must have a verb unless we have a destination
        if error == None and cheat == None:
            for idx, word in enumerate(words):
                for alias_array in VERB_ALIASES:
                    for verb_alias in alias_array:
                        num_words_in_alias = len(verb_alias.split())
                        words_sublist = words[idx: (idx + num_words_in_alias)]
                        words_sublist_string = ' '.join(words_sublist)
                        #remove punctuation, won't affect indexing
                        words_sublist_string = ''.join(ch for ch in words_sublist_string if ch not in string.punctuation)
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
        
        # VERB special GO: set an empty verb to GO if we have a destination, else leave for error checking
        if error == None and cheat == None and verb == None and noun_is == 'destination':
            verb_is_special = True
            verb = GO
            
        # VERB special SPRAYPAINT check: the model is VERB(SPRAYPAINT)->TARGET 
        if error == None and cheat == None and verb_is_special == False:
            #TARGET must be a message string
            if verb == SPRAYPAINT:
                words = sprayCommand.split()
                if verb_idx + 1 < len(words):
                    verb_is_special = True
                    words_sublist = words[verb_idx + 1:]
                    target = ' '.join(words_sublist)
                    target_is = 'message'
                else:
                    error = INVALID_SPRAYPAINT_NO_MESSAGE
        
        # ERROR Check:
        if error == None and cheat == None:
            # VERB NONE Check:
            if verb == None:
                error =  INVALID_NO_VERB
            # VERB DESTINATION check:
            elif verb == GO and noun_is != 'destination':
                error = INVALID_GO_NO_DESTINATION
            elif (verb != None and verb != GO) and noun_is == 'destination':
                error = INVALID_DESTINATION_WRONG_VERB
            # NEGATION Check: If we have a non special verb sentence, there shouldn't be any negations
            elif verb_is_special == False:
                for word in words:
                    if word in NEGATIONS:
                        error = INVALID_NEGATION
            

        # SUBJECT or PREPOSTION check: the model is VERB-> (PREPOSITION ANY SUBSEQUENT LOCATION) + NOUN-> TARGET
        if error == None and cheat == None and verb_is_special == False:
        
            words = words[verb_idx + 1: ]
        
            # for each word in the remaining string, check if noun (object or feature) or preposition
            for idx, word in enumerate(words):
            
                #PREPOSITION check
                for prep_name in PREPOSITIONS:
                    # check number of words in name so we can compare correct number of words from command
                    num_words_in_name = len(prep_name.split())
                    words_sublist = words[idx: idx + num_words_in_name]
                    words_sublist_string = ' '.join(words_sublist)
                    words_sublist_string = ''.join(ch for ch in words_sublist_string if ch not in string.punctuation)
                    if words_sublist_string == prep_name:
                        if preposition == None:
                            preposition = words_sublist_string
                            prep_idx = last_idx = idx + num_words_in_name - 1 
                        # currently can only use one
                        else:
                            error = INVALID_EXTRA_PREPOSITIONS
                #NOUN and TARGET checks
                for obj_alias_array in OBJECT_ALIASES:
                    for obj_alias in obj_alias_array:
                        # check number of words in alias so we can compare correct number of words from command
                        num_words_in_alias = len(obj_alias.split())
                        words_sublist = words[idx: idx + num_words_in_alias]
                        words_sublist_string = ' '.join(words_sublist)
                        words_sublist_string = ''.join(ch for ch in words_sublist_string if ch not in string.punctuation)
                        if words_sublist_string == obj_alias:
                            # only save  the first occurrence of object or feature
                            if noun == None:
                                # the alias arrays always store the base word at index 0
                                noun = str(obj_alias_array[0])
                                noun_is = 'object'
                                #last index is the last index of the last noun or target we found
                                noun_idx = last_idx = idx + num_words_in_alias - 1 
                            # second occurrence will be the target and cannot also be the noun
                            elif target == None and noun != str(obj_alias_array[0]):
                                target = str(obj_alias_array[0])
                                target_is = 'object'
                                targ_idx = last_idx = idx + num_words_in_alias - 1 
                            # current index must > last one we found a noun or target in
                            elif idx > last_idx:
                                if str(obj_alias_array[0]) == noun or str(obj_alias_array[0]) == target:
                                    error = INVALID_DOUBLE
                                else:
                                    error = INVALID_EXTRA_NOUNS
                            # else it is just a double, such as 'floppy disk' which could be 'floppy' and 'disk'
                                
                for feat_alias_arrays in FEATURES_ALIASES_ARRAYS:
                    for feat_alias_array in feat_alias_arrays:
                        for feat_alias in feat_alias_array:
                            num_words_in_name = len(feat_alias.split())
                            words_sublist = words[idx: idx + num_words_in_name]
                            words_sublist_string = ' '.join(words_sublist)
                            words_sublist_string = ''.join(ch for ch in words_sublist_string if ch not in string.punctuation)
                            if words_sublist_string == feat_alias:
                                if noun == None:
                                    noun = str(feat_alias_array[0])
                                    noun_is = 'feature'
                                    noun_idx = last_idx = idx + num_words_in_name - 1 
                                elif target == None and noun != str(feat_alias_array[0]):
                                    target = str(feat_alias_array[0])
                                    target_is = 'feature'
                                    targ_idx = last_idx = idx + num_words_in_name - 1 
                                elif idx > last_idx:
                                    if str(feat_alias_array[0]) == noun or str(feat_alias_array[0]) == target:
                                        error = INVALID_DOUBLE
                                    else:
                                        error = INVALID_EXTRA_NOUNS


            #INVALID SENTENCE STRUCTURE check: check for these if not handled by special verbs above:
            if verb_is_special == False:
                #INVALID: VERB NOUN PREP (no TARGET)
                if noun != None and preposition != None and target == None:
                    if prep_idx > noun_idx:
                        error = INVALID_SENTENCE_STRUCTURE
        
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


        return R
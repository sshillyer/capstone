# DELPHINUS - ADVENTURE APP
# CS 467 - Winter 2017
# Team Members: Sara Hashem, Shawn Hillyer, Niza Volair
#
# language_parser_wrapper.py
# Description: Wraps the return values from LanguageParser
# Created by Shawn to interface between parser and GameClient; maintained by Shawn and Niza
#
# CITATIONS
# CITE:



# DEV NOTES: Here's how this would be used in LanguageParser:
#
# results = LanguageParserWrapper
# results.set_verb(STEAL)
# results.set_noun("graphics card", OBJECT_TYPE)    # Need to define OBJECT_TYPE in the 'language_words.py' file
#
# You could also add extras. Let's say you had 3 extras, you could do a loop:
# for subject in extras:
#     results.append_extra(subject.name, subject.type)

class LanguageParserWrapper:
    def __init__(self):
        self.verb = None
        self.noun = {}
        self.extras = []
        self.preposition = None
        self.error_message = None

    def __str__(self):
        '''
        override str() method for debug purposes
        :return:
        '''
        str = "{\n\t'verb' : '" + self.verb + "'\n"
        if self.noun is None:
            str+= "\t'noun['name']' : None'\n"
        else:
            str += "\t'noun['name']' : '" + self.noun['name'] + "'\n"
            str += "\t'noun['type']' : '" + self.noun['type'] + "'\n"
        str += "\t'extras' : "

        if self.extras:
            for extra in self.extras:
                str += "\n\t{\n['name' : '" + extra['name'] + "']\n"
                str += "\t['type' : '" + extra['type'] + "']\n},"
        else:
            str+= "\t\tNone\n"

        str += "\t'preposition' : "
        try:
            str += "'" + self.preposition + "'\n"
        except:
            str += "None\n"

        str += "\t'error_message' : "
        try:
            str += "'" + self.error_message + "'\n"
        except:
            str += "None\n"

        str += "}"
        return str

    def set_verb(self, verb_string):
        self.verb = verb_string

    def set_noun(self, noun_name_string, noun_type_string):
        self.noun['name'] = noun_name_string
        self.noun['type'] = noun_type_string

    def set_extra(self, extra_name_string, extra_type_string):
        new_extra = {
            'name' : extra_name_string,
            'type' : extra_type_string
        }

        self.extras.append(new_extra)

    def set_preposition(self, preposition_string):
        self.preposition = preposition_string

    def set_error_message(self, error_message):
        self.error_message = error_message

    def get_verb(self):
        return self.verb

    def get_noun(self):
        return self.noun

    def get_extras(self):
        return self.extras

    def get_preposition(self):
        return self.preposition

    def get_error_message(self):
        return self.error_message
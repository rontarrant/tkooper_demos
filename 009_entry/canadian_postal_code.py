# Handle Canadian Postal Codes

class CheckPostalCode:
	def check_postal_code(postal_input, strictCapitalization = False, fixSpace = True):
		'''
		Returns a Tuple of (boolean, string):
		- (True, postal_code) or 
		- (False, error message) 
		By default lower and upper case characters are allowed,  
		a missing middle space will be substituted.
		Adapted by Ron Tarrant
		Original Author: Patrick Artner (https://stackoverflow.com/users/7505395/patrick-artner)
		'''
		postal_code = postal_input.strip()                   # copy postal_input, strip whitespaces front/end

		if fixSpace and len(postal_code) == 6:
			postal_code = postal_code[0:3] + " " + postal_code[3:]      # if allowed and needed, insert missing space

		permitted_numbers = "0123456789"              # allowed numbers
		alph = "ABCEGHJKLMNPRSTVWXYZ"    # allowed characters (WZ handled below)
		numeric_indices = [1,4,6]             # index of number
		alpha_indices = [0,2,5]             # index of character (WZ handled below)

		illegalCharacters = [x for x in postal_code if x not in (permitted_numbers + alph.lower() + alph + " ")]

		if strictCapitalization:
			illegalCharacters = [x for x in postal_code if x not in (alph + permitted_numbers + " ")]

		if illegalCharacters:
			return(False, "Illegal characters detected: " + str(illegalCharacters))

		postalCode = [x.upper() for x in postal_code]           # copy to uppercase list

		if len(postalCode) != 7:                      # length-validation
			return (False, "Length not 7")

		for index in range(0, len(postalCode)):          # loop over all indices
			character = postalCode[index]
		  
			if character in permitted_numbers and index not in numeric_indices:  # is s number, charactereck index
				return (False, "Format not 'ADA DAD'")     
			elif character in alph and index not in alpha_indices: # id s character, check index
				return (False, "Format not 'ADA DAD'") # alpha / digit
			elif character == " " and index != 3:               # is space in between
				return (False, "Format not 'ADA DAD'")

		if postalCode[0] in "WZ":                      # no W or Z first char
			return (False, "Cant start with W or Z")

		return (True,"".join(postalCode))    # yep - all good

import authorization
import json
import requests
import search
import my_parser
import sys

from urls import *


def main():
	auth = authorization.authorize()
	arg_parser = my_parser.make_parser()
	arguments = arg_parser.parse_args(sys.argv[1:])
	#Convert parsed arguments from Namespace to dictionary
	arguments = vars(arguments)
	#Remove command from the arguments dictionary and store it as a variable
	command = arguments.pop("command")
	print arguments

	if command == "search":
		result = search.search(arguments['query'],arguments['result_type'], arguments['count'], auth)
		print json.dumps(result.json(), indent=4)

if __name__ == "__main__":
	main()



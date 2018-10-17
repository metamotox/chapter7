# -*- coding:utf-8 -*-

import run(**args):
	print "[*] In environment module."
	return str(os.environ)
	# os.environ : refer to environment variables
	#  os.environ shows environment variables as mapped object
	# e.g.) os.environ["HOME"] -> /home/forensic
	#        above is equals to "printenv | grep HOME

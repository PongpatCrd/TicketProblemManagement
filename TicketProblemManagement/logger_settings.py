LOGGING = {
	'version':1,
	'disable_existing_loggers': False,
	'formatters':{
		'large':{
			'format':'%(asctime)s  %(levelname)s  %(process)d  %(pathname)s  %(funcName)s  %(lineno)d  %(message)s  '
		},
		'tiny':{
			'format':'%(asctime)s  %(message)s  '
		}
	},
	'handlers':{
		'errors_file':{
			'level':'WARNING',
		       'class':'logging.handlers.FileHandler',
			'mode'='a',
			'filename':'ErrorLoggers.log',
			'formatter':'large',
		},
	},
	'loggers':{
		'error_logger':{
			'handlers':['errors_file'],
			'level':'WARNING',
			'propagate':False,
		},
	},
}
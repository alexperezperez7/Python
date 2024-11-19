import locale

current_local_configuration = locale.getlocale()
print('Current local configuration is:', current_local_configuration)

default_local_configuration = locale.getdefaultlocale()
print('Default local configuration is:', default_local_configuration)

current_encoding = locale.getpreferredencoding()
print('Current encoding is:', current_encoding)

calendar_format = locale.nl_langinfo(locale.D_FMT)
print('The calendar date format is:', calendar_format)

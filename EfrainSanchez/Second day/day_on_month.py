from time import gmtime, strftime
import calendar
#print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
ano = strftime("%Y", gmtime())
dias = calendar.monthrange(ano,1)
print(dias)
#'Thu, 28 Jun 2001 14:17:15 +0000'
# Data acquired from http://www.bom.gov.au/climate/dwo/IDCJDW3052.latest.shtml
# Direct link
# http://www.bom.gov.au/climate/dwo/201711/text/IDCJDW3052.201711.csv


with open("IDCJDW3052.201711.csv") as csv:
    data = csv.read().splitlines(True)

with open("parsed.csv", 'w') as csv:
    csv.writelines(data[6:])

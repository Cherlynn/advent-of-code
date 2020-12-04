
required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

passports = [""]
passports_formatted = []

inputfile_name = "aoc_2020_4"
inputfile = open(inputfile_name, "r")
lines = inputfile.readlines()
inputfile.close()

counter = 0
for line in lines:
    if line != "\n":
        passports[counter] = passports[counter] + " " + line.rstrip()
    else:
        counter += 1
        passports.append("")

for passport in passports:
    fields = {field.split(":")[0]:field.split(":")[1] for field in passport.split()}
    passports_formatted.append(fields)

count = 0
for passport_formatted in passports_formatted:
    if all(required_field in passport_formatted for required_field in required_fields):
        count += 1

print(count)

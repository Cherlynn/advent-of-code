import re

def validate_fields(fields):

    #byr
    byr = fields["byr"]
    if re.match("[0-9]{4}", byr) is None:
        return False
    if int(byr) < 1920 or int(byr) > 2002:
        return False

    #iyr
    iyr = fields["iyr"]
    if re.match("[0-9]{4}", iyr) is None:
        return False
    if int(iyr) < 2010 or int(iyr) > 2020:
        return False

    #eyr
    eyr = fields["eyr"]
    if re.match("[0-9]{4}", eyr) is None:
        return False
    if int(eyr) < 2020 or int(eyr) > 2030:
        return False

    #hgt
    hgt = fields["hgt"]
    if re.match("[0-9]{3}cm", hgt) is not None:
        num = int(re.search("([0-9]{3})cm", hgt).group(1))
        #print(hgt)
        if num < 150 or num > 193:
            return False
    elif re.match("[0-9]{2}in", hgt) is not None:
        num = int(re.search("([0-9]{2})in", hgt).group(1))
        if num < 59 or num > 76:
            return False
    else:
        return False

    #hcl
    hcl = fields["hcl"]
    if re.match("#[a-f0-9]{6}", hcl) is None:
        return False

    #ecl
    possible_values = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    ecl = fields["ecl"]
    if ecl not in possible_values:
        return False

    #pid
    pid = fields["pid"]
    if re.match("[0-9]{9}$", pid) is None:
        return False

    return True


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
        values_are_valid = validate_fields(passport_formatted)
        if values_are_valid:
            count += 1

print("Count:", count)

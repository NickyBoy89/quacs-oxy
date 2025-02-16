"""
# transform_to_rpi.py transforms some quirks of the OXY format of classes into the RPI format
"""

semesters = []

with open("semesters.json") as semesters_file:
    semesters = semesters_file.readlines()

formatted_semesters = []

for semester in semesters:
    # Skip blank lines
    if len(semester) == 0:
        continue

    # Read the semester code
    # Ex: 202401 transforms into 2024 (year) + 01 (semester code)

    assert len(semester) == 6
    year = semester[:4]
    semester_code = semester[:-2]

    # OXY chooses different semester codes than RPI, notably:
    # * 01 -> Fall
    # * 02 -> Spring
    # * 03 -> Summer
    #
    # While RPI uses the month, so:
    # * 09 -> Fall
    # * 01 -> Spring
    # * 05 -> Summer

    match semester_code:
        case "01":
            formatted = year + "09"
        case "02":
            formatted = year + "01"
        case "03":
            formatted = year + "05"
        case _:
            raise Exception(
                f"Unable to convert OXY semester code {semester_code} into its RPI equivalent"
            )

    formatted_semesters.append(formatted)

# Overwrite the previous semesters file
with open("semesters.json", "w") as outfile:
    outfile.writelines(formatted_semesters)

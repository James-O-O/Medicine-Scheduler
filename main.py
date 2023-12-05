from fpdf import FPDF

data = [["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]]
monday_meds = []
tuesday_meds = []
wednesday_meds = []
thursday_meds = []
friday_meds = []

name = (input("Please Enter A Name: ").capitalize())

print("**** ENTER EACH MEDICINE THAT IS TO BE TAKEN **** \n")
print("**** THEN ENTER THE DAY OF WEEK IT IS TO BE TAKEN*** \n")
print("**** ENTER 'STOP' WHEN YOU ARE DONE **** \n")


def empty_cell_check(cellLength):
    if len(cellLength) <= 4:
        return 5 - len(cellLength)
    else:
        return 0


while True:
    med = (input("Enter a medicine name").capitalize())
    if med == 'Stop':
        if len(monday_meds) == 1:
            data.append(monday_meds)
        if len(monday_meds) >= 2:
            for x in range(len(monday_meds)):
                data.append(list(monday_meds[x]))

        if len(tuesday_meds) > 0:
            for x in range(len(tuesday_meds)):
                try:
                    data[x + 1].append(tuesday_meds[x])
                except:
                    data.append([''])
                    data[x + 1].append(tuesday_meds[x])

        if len(wednesday_meds) > 0:
            for x in range(len(wednesday_meds)):
                try:
                    data[x + 1].insert(2, wednesday_meds[x])

                except:

                    if len(data) == 1:
                        data.append(['', ''])

                        data[x + 1].append(wednesday_meds[x])
                    if type(data[x + 1][0]) == type(name):
                        data[x + 1].append('')
                        data[x + 1].append(wednesday_meds[x])
        if len(thursday_meds) > 0:
            for x in range(len(thursday_meds)):
                try:
                    data[x + 1].insert(3, thursday_meds[x])

                except:

                    if len(data) == 1:
                        data.append(['', '', ''])

                        data[x + 1].append(thursday_meds[x])
                    if len(data[x + 1]) == 1:
                        print('cond 3')
                        data[x + 1].append('')
                        data[x + 1].append('')
                        data.append(thursday_meds[x])

                    if type(data[x + 1][1]) == type(name):
                        print('cond 4')
                        data[x + 1].append('')
                        data[x + 1].append(wednesday_meds[x])
        if len(friday_meds) > 0:
            for x in range(len(friday_meds)):
                data.append(['', '', '', ''])
                data[x + 1].append(friday_meds[x])

        for x in range(len(data)):
            empty_space = empty_cell_check(data[x])

            for y in range(int(empty_space)):
                data[x].append(" ")

        break
    else:
        day = input("Enter day:")
        day = day.capitalize()
        if day == "Monday":
            monday_meds.append(med)
        if day == "Tuesday":
            tuesday_meds.append(med)
        if day == "Wednesday":
            wednesday_meds.append(med)
        if day == "Thursday":
            thursday_meds.append(med)
        if day == "Friday":
            friday_meds.append(med)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Times", size=10)
line_height = pdf.font_size * 2.5
col_width = pdf.epw / 5
with pdf.table() as table:
    for data_row in data:
        row = table.row()
        for datum in data_row:
            row.cell(datum)
pdf.output(f"{name}'s Medicine Schedule.pdf")

import csv
import datetime
import json
import pickle
import re
import xlrd
import shelve


class ValidationError(Exception):
    def __init__(self, message=''):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class FileFormatError(ValidationError):
    pass


class EmailFormatError(ValidationError):
    pass


class UserNameFormatError(ValidationError):
    pass


class DateFormatError(TypeError):
    pass


class FileConverter:
    def __init__(self, excel_file):
        self.excel_file = excel_file
        self.data = []
        self.keys = []
        self.errors = []

    def get_data(self, sheetid=0):
        book = xlrd.open_workbook(self.excel_file)
        sheet = book.sheet_by_index(sheetid)
        self.keys = [sheet.cell_value(sheetid, col) for col in range(sheet.ncols)]
        self.data = [dict(zip(self.keys, [sheet.cell_value(r, c) for c in range(sheet.ncols)])) for r in
                     range(1, sheet.nrows)]
        return self.data

    def check_and_format_d(self, dformat="%d/%m/%Y"):
        for i in range(len(self.data)):
            try:
                if type(self.data[i]['Joined']) != float:
                    raise DateFormatError
                else:
                    time_tuple = xlrd.xldate_as_tuple(self.data[i]['Joined'], 0)
                    self.data[i]['Joined'] = datetime.datetime(*time_tuple).strftime(dformat)
            except DateFormatError:
                if self.data[i] not in self.errors:
                    self.errors.append(self.data[i])

    def check_email(self):
        valid_mail = r'^[a-zA-Z\d.]+@(?:[a-zA-Z\d]+\.){1,2}[a-zA-Z\d]+$'
        for i in range(len(self.data)):
            try:
                if bool(re.match(valid_mail, self.data[i]['Email'])) is False:
                    raise EmailFormatError
            except EmailFormatError:
                if self.data[i] not in self.errors:
                    self.errors.append(self.data[i])

    def check_username(self):
        for i in range(len(self.data)):
            try:
                if bool(re.match('^[a-zA-Z]+$', self.data[i]['Username'])) is False:
                    raise UserNameFormatError
            except UserNameFormatError:
                if self.data[i] not in self.errors:
                    self.errors.append(self.data[i])

    def update_data(self):
        self.data = [item for item in self.data if item not in self.errors]

    def write_json(self):
        with open(self.excel_file.split('.')[0] + '.json', 'w') as jf:
            json.dump(self.data, jf)

    def write_csv(self):
        with open(self.excel_file.split('.')[0] + '.csv', 'w', encoding='utf-8') as csv_file:
            dict_writer = csv.DictWriter(csv_file, self.keys)
            dict_writer.writeheader()
            dict_writer.writerows(self.data)

    def write_pickle(self):
        with open(self.excel_file.split('.')[0] + '.bin', 'wb') as pickle_file:
            pickle.dump(self.data, pickle_file)

    def write_shelve(self):
        d = shelve.open(self.excel_file.split('.')[0])
        for i in range(len(self.data)):
            for k, v in self.data[i].items():
                d[self.data[i][k]] = v
        d.close()

    def write_errors(self):
        with open('errors.txt', 'w') as errors:
            json.dump(self.errors, errors)


obj = FileConverter("table.xlsx")
obj.get_data()
obj.check_and_format_d()
obj.check_email()
obj.check_username()
obj.update_data()
obj.write_csv()
obj.write_json()
obj.write_pickle()
obj.write_shelve()
obj.write_errors()
print(obj.data)
print(obj.errors)

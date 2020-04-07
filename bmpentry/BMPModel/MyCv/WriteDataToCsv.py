import pandas as pd

class WriteDataToCsv:
    def __init__(self, file_path="result.first_csv"):
        self.columns = ["NO", "All", "Red", "Green", "Result"]
        self.file_path = file_path
        self.result_list = []

    def appendData(self, val1, val2, val3, val4, val5):
        self.result_list.append([val1, val2, val3, val4, val5])

    def write(self):
        dt = pd.DataFrame(self.result_list, columns=self.columns)
        dt.to_csv(self.file_path, index=0)




# result_list = [['1', 1, 1], ['2', 2, 2], ['3', 3, 3]]
# columns = ["URL", "predict", "score"]
# dt = pd.DataFrame(result_list, columns=columns)
# dt.to_excel("result_xlsx.xlsx", index=0)
# dt.to_csv("resultA.first_csv", index=0)

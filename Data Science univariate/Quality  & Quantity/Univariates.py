class Univariate():
    def quaQual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            #print(columnName)
            if (dataset[columnName].dtype=='str'):
               # print("qual")
                qual.append(columnName)
            else:
               # print("quan")
                quan.append(columnName)
        return quan,qual
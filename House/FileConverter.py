
# 각 컬럼별 항목을 분리할 리스트
class ItemInfo:
    index_ = -1
    itemList_ = []

    def __init__(self, index):
        self.index_ = index
        self.itemList_ = []

    def isExistItem(self, find_string):
        for item in self.itemList_:
            if find_string == item:
                return True

        return False

    def appendItem(self, new_string):
        if self.isExistItem(new_string) == True:
            return False

        self.itemList_.append(new_string)

        return True

    def showItems(self):
        for item in self.itemList_:
            print (item)

# 파일 변환기
class FileDataConverter:
    inputFilename_ = ""
    outputFilename_ = ""
    itemInfos_ = []

    def __init__(self, inputFilename, outputFilename):
            self.inputFilename_ = inputFilename
            self.outputFilename_ = outputFilename
            self.itemInfos_ = []

    def getItemInfo(self, index):
        for itemInfo in self.itemInfos_:
            if itemInfo.index_ == index:
                return itemInfo

        return None

    def showItemInfos(self):
        for itemInfo in self.itemInfos_:
            print("#####", itemInfo.index_, "########")
            itemInfo.showItems()

    def analysis(self):
        isFirstLine = True

        # 파일에서 line 별로 데이터를 읽어 드림
        for line in open(self.inputFilename_):

            # 첫 번째 라인은 타이틀이기 때문에 제외
            if isFirstLine is True:
                isFirstLine = False
                continue

            # split the text
            words = line.rstrip('\n').split(",")

            # for each word in the line:
            for index, word in enumerate(words):
                # 숫자가 아닌 경우에는 아이템의 인덱스별로 데이터를 추가함
                if word.isdigit() != True:
                    itemInfo = self.getItemInfo(index)

                    if itemInfo is None:
                        newItemInfo = ItemInfo(index)

                        self.itemInfos_.append(newItemInfo)

                        itemInfo = newItemInfo

                    itemInfo.appendItem(word)

                    # print the word
                    # print(index, word)

        self.showItemInfos()

# 각 항목별 리스트를 정리
x = FileDataConverter("train.csv", "converted_train.csv")

x.analysis()

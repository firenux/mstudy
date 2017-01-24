
# 각 컬럼별 항목을 분리할 리스트
class ItemInfo:
  index = -1
  item_type = 0 # 0: Number, 1: String

  min_val = -1.0
  max_val = -1.0
  itemList = []

  def __init__(self, index, item_type):
    self.index = index
    self.item_type = item_type
    self.itemList = []

  def isExistItem(self, find_string):
      for item in self.itemList:
          if find_string == item:
              return True

      return False

  def appendItem(self, new_string):
    if new_string.isdigit() != True:
      self.min_val = 0

      if self.isExistItem(new_string) == True:
          return False

      self.itemList.append(new_string)
      # self.max_val = size(self.itemList)
    else:
      new_value = float(new_string)

      if self.min_val == -1 or self.min_val > new_value:
        self.min_val = new_value

      if self.max_val == -1 or self.max_val < new_value:
        self.max_val = new_value

    return True

  def showItems(self):
    if self.item_type is 0:
      print ("Max: ", self.max_val, ", Min: ", self.min_val)
    else:
        for item in self.itemList:
          print (item)

        print ("Max: ", self.max_val, ", Min: ", self.min_val)


# 파일 변환기
class FileDataConverter:
  _inputFilename = ""
  _outputFilename = ""
  _itemInfos = []

  def __init__(self, inputFilename, outputFilename):
    self._inputFilename = inputFilename
    self._outputFilename = outputFilename
    self._itemInfos = []

  def getItemInfo(self, index):
    for itemInfo in self._itemInfos:
      if itemInfo.index == index:
          return itemInfo

    return None

  def showItemInfos(self):
    for itemInfo in self._itemInfos:
      print("#####", itemInfo.index, "########")
      itemInfo.showItems()

  def analysis(self):
    isFirstLine = True

    # 파일에서 line 별로 데이터를 읽어 드림
    for line in open(self._inputFilename):
      # 첫 번째 라인은 타이틀이기 때문에 제외
      if isFirstLine is True:
        isFirstLine = False
        continue

      # split the text
      words = line.rstrip('\n').split(",")

      # for each word in the line:
      for index, word in enumerate(words):
        # 숫자가 아닌 경우에는 아이템의 인덱스별로 데이터를 추가함
        itemInfo = self.getItemInfo(index)

        if itemInfo is None:
          item_type = 0

          if word.isdigit() != True:
            item_type = 1

          newItemInfo = ItemInfo(index, item_type)
          self._itemInfos.append(newItemInfo)
          itemInfo = newItemInfo

        itemInfo.appendItem(word)

    self.showItemInfos()

# 각 항목별 리스트를 정리
x = FileDataConverter("train.csv", "converted_train.csv")

x.analysis()

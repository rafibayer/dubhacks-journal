from src.textRecorder import TextRecorder

DATA_LOCATION = "src/text_data/"

class TRUnitTests:

    @staticmethod
    def testNoFilePath():
        myTR = TextRecorder()


    @staticmethod
    def testLoadFromFile():
        myTR = TextRecorder(DATA_LOCATION + "2019-10-12.txt")

    @staticmethod
    def testSerializeAndLoad():
        myTR = TextRecorder(DATA_LOCATION + "2019-10-12.txt")
        data = myTR.data
        myTR.serialize_data(myTR.filepath)

        myTR2 = TextRecorder(DATA_LOCATION + "2019-10-12.txt")
        data2 = myTR.data

        assert(data == data2)

       
    @staticmethod
    def testAddNone():
        myTR = TextRecorder(DATA_LOCATION + "test.txt")
        myTR.add_entry(None)
       
    @staticmethod
    def testAddEmpty():
        myTR = TextRecorder(DATA_LOCATION + "test.txt")
        myTR.add_entry("")
       
    @staticmethod
    def testEditToNone():
        myTR = TextRecorder(DATA_LOCATION + "test.txt")
        myTR.edit_entry(0, None)
       
    @staticmethod
    def testAppendNonString():
        myTR = TextRecorder(DATA_LOCATION + "test.txt")
        myTR.append_entry(0, None)
       
    @staticmethod
    def testGetDNE():
        myTR = TextRecorder(DATA_LOCATION + "test.txt")
        myTR.get_entry(100)
       
    @staticmethod
    def testClearDNE():
        myTR = TextRecorder(DATA_LOCATION + "test.txt")
        myTR.clear_entry(100)


TRUnitTests.testAddEmpty()
TRUnitTests.testAddNone()
TRUnitTests.testAppendNonString()
TRUnitTests.testClearDNE()
TRUnitTests.testEditToNone()
TRUnitTests.testGetDNE()
TRUnitTests.testLoadFromFile()
TRUnitTests.testNoFilePath()
TRUnitTests.testSerializeAndLoad()

print("all unit tests run succesfully :')")

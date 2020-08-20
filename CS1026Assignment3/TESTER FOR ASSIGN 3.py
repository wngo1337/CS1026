# CS 1026 Assignment 3 - Sentiment Analysis
# code written by William Ngo

import happy_histogram

# create dictionary to store keywords with value that will be read
keyWords = {}
zoneValues = {}

# function to read in keywords to dictionary
def keyReader():
    fileName = input("Enter the name of the keywords file: ")
    try:
        keyFile = open(fileName, "r", encoding="utf-8") # input error may occur on this line
    except IOError as badInput:
        print("{} is not a valid file name, good night.".format(badInput))
        exit()

    for line in keyFile:
        myLine = line.rstrip().split(",")
        keyWords[myLine[0]] = int(myLine[1])
    print(keyWords)
    keyFile.close()

# function to read tweets and compare them to dictionary
def tweetReader():
    fileName2 = input("Enter the name of the tweets file: ") # input error may occur on this line
    try:
        tweetFile = open(fileName2, "r", encoding="utf-8")
    except IOError as badInput2:
        print("{} cannot be found, try again next time :(".format(badInput2))
        exit()

    # declaring variables for later use in the function
    pacificHappy = 0
    pacificNum = 0
    mountainHappy = 0
    mountainNum = 0
    centralHappy = 0
    centralNum = 0
    easternHappy = 0
    easternNum = 0

    # separate lines into latitude, longitude, value, date, time, and then the text we want
    # we only need the list values with index of 0, 1, and 5 (which we will break down into words)
    for tweet in tweetFile:
        totalHappiness = 0
        happyAvg = 0
        numWords = 0
        tweet = tweet.rstrip()
        tweet = tweet.split(" ", 5)

        # clean up latitude and longitude values (methods left unchained for clarity)
        tweet[0] = tweet[0].replace(",", "")
        tweet[0] = tweet[0].replace("[", "")
        # assign latitude and longitude values
        latitude = float(tweet[0])
        tweet[1] = tweet[1].replace("]", "")
        longitude = float(tweet[1])

        tweetContent = tweet[5]

        # create a new list to analyze the words of each tweet
        tweetWords = tweetContent.split()

        for word in tweetWords:
            # convert all words to lowercase and strip symbols
            word = word.lower()
            word = word.strip("~.,!:?#")
            print(word)
            # if word is a keyword count the word and add its value to happiness of tweet
            if word in keyWords:
                numWords = numWords + 1
                value = keyWords[word]
                totalHappiness = totalHappiness + value

        # only totals if happiness > 0 and we are in the right latitude
        if totalHappiness > 0 and latitude >= 24.660845 and latitude <= 49.189787:
            happyAvg = totalHappiness / numWords

            # add the happiness score to the appropriate timezone and add 1 to the tweet count
            if longitude <= -67.444574 and longitude >= -87.518395:
                easternHappy = easternHappy + happyAvg
                easternNum = easternNum + 1

            elif longitude < -87.518395 and longitude >= -101.998892:
                centralHappy = centralHappy + happyAvg
                centralNum = centralNum + 1

            elif longitude < -101.998892 and longitude >= -115.236428:
                mountainHappy = mountainHappy + happyAvg
                mountainNum = mountainNum + 1

            elif longitude < -115.236428 and longitude >= -125.242264:
                pacificHappy = pacificHappy + happyAvg
                pacificNum = pacificNum + 1

            else:
                pass # tweet doesn't have the right longitude or has no key words

    # calculate the happiness scores of each region and print them
    pacificHappyAvg = round(pacificHappy / pacificNum, 3)
    mountainHappyAvg = round(mountainHappy / mountainNum, 3)
    centralHappyAvg = round(centralHappy / centralNum, 3)
    easternHappyAvg = round(easternHappy / easternNum, 3)

    # assigning the keys of our dictionary to lists
    zoneValues["pacific"] = []
    zoneValues["mountain"] = []
    zoneValues["central"] = []
    zoneValues["eastern"] = []

    # adding the important values to their respective key (list)
    zoneValues["pacific"].extend([pacificHappyAvg, pacificNum])
    zoneValues["mountain"].extend([mountainHappyAvg, mountainNum])
    zoneValues["central"].extend([centralHappyAvg, centralNum])
    zoneValues["eastern"].extend([easternHappyAvg, easternNum])

# call function to see if it works lol
def main():
    keyReader()
    tweetReader()

    # print all the information in our zoneValues dictionary
    for key in zoneValues:
        print("The happiness score for the {} timezone is {}, and we found {} tweets in its range".format(key, zoneValues[key][0], zoneValues[key][1]))

#    calling the drawSimpleHistogram function from happy_histogram
    happy_histogram.drawSimpleHistogram(zoneValues["pacific"][0], zoneValues["mountain"][0], zoneValues["central"][0], zoneValues["eastern"][0])

# call main to run
main()

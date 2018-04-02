from numpy import loadtxt

anomali_dict = {}
#/TR/ardışık her iki noktanın ortalamasını tutmak için oluşturdum
#/ENG/to keep the average of both consecutive points
avg_list = []
counter = 0

class Anomali():
    def __init__(self, x, y, counter):
        self.x = x
        self.y = y
        self.counter = counter

    def averagePoints(self):

        while(self.counter < 4999):
            avgX = (self.x[self.counter] + self.x[self.counter + 1]) / 2
            avgY = (self.y[self.counter] + self.y[self.counter + 1]) / 2
            avg_list.append((avgX, avgY))

            self.counter = self.counter + 1

        self.checkAnomali(avg_list)

    def checkAnomali(self, avg_list):
        anomali_counter = 0
        counter = 0

        #/TR/ardaşık her iki noktanın birbirine uzaklıkları
        #/ENG/distances between successive points
        while(counter<4998):
            distance = ((avg_list[counter + 1][1] - avg_list[counter][1]) ** 2 + (avg_list[counter + 1][0] - avg_list[counter][0]) ** 2) ** 0.5
            anomali_dict[avg_list[counter],avg_list[counter + 1]] = distance
            counter = counter + 1

        for key, val in anomali_dict.items():
            if val > 100:
                anomali_counter = anomali_counter + 1
                print("Anomali_{0},{1}".format(anomali_counter,key))

                #/TR/Anomali olan noktaları kaydet
                #/ENG/Save points with anomalies
                with open("anomali_tespit/AnomaliTespit.csv", "a") as dosya:
                    dosya.write("Anomali_{0},{1}\n".format(anomali_counter,key))

def main():
    data = loadtxt(
        'Sample5000Points.txt',
        delimiter=','
    )

    x = data[:, 0]
    y = data[:, 1]

    call_class = Anomali(x, y, counter)
    call_class.averagePoints()

if __name__ == "__main__":
    main()

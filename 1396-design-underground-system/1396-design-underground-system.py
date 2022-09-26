class UndergroundSystem(object):

    def __init__(self):
        self.customer_database = {}
        self.station_database = {}

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        customer_entry = {stationName: t}
        self.customer_database[id] = customer_entry
        
    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        customer_entry = self.customer_database[id]
        checkin_station, checkin_time = customer_entry.items()[0]
        duration = t - checkin_time
        if checkin_station in self.station_database:
            entry = self.station_database[checkin_station]
            if stationName in entry:
                #if someone has finished the same journey before
                time_list = entry[stationName]
                time_list.append(duration)
                entry[stationName]=time_list
                self.station_database[checkin_station] = entry
            else:
                #if previous customers have completed journeys starting from the same checkinStation but no one completed a journey to the checkout station
                entry[stationName] = [duration]
        else:
            #no one ever complete a journey involving either checkin-station and checkout-station
            entry = {stationName: [duration]}
            self.station_database[checkin_station] = entry
            
    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        
        entry = self.station_database[startStation]                
        time_list = entry[endStation]
        print(time_list)
        sum = 0
        for item in time_list:
            sum += item
        
        return float(sum) / len(time_list)
    
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
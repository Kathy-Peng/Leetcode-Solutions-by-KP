class UndergroundSystem(object):

    def __init__(self):
        self.arrival_info = {}
        self.total = {}

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        #when checking in customers we only update the arrival_info table
        #we store the stationName and checkin time with the customer id as key
        self.arrival_info[id] = [stationName,t]
        
    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        checkin_station = self.arrival_info[id][0]
        checkin_time = self.arrival_info[id][1]
        if (checkin_station,stationName) not in self.total:
            self.total[(checkin_station,stationName)] = [t-checkin_time, 1]
        else:
            entry = self.total[(checkin_station,stationName)]
            new_entry = [entry[0]+(t-checkin_time), entry[1]+1]
            self.total[(checkin_station,stationName)] = new_entry
            
    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        entry = self.total[(startStation,endStation)]
        total_time = entry[0]
        count = entry[1]
        return float(total_time)/count
        
    
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
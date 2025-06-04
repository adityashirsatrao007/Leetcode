# Last updated: 6/4/2025, 9:19:46 PM
class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        start_time=customers[0][0]+customers[0][1]
        wait_time=start_time-customers[0][0]
        res=wait_time
        for i in range(1,len(customers)):
            if(start_time<customers[i][0]):
                start_time=customers[i][0]+customers[i][1]
                wait_time=wait_time=start_time-customers[i][0]
            else:

                start_time+=customers[i][1]
                wait_time=start_time-customers[i][0]
                
            res+=wait_time

    
        return res/float(len(customers))
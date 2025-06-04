# Last updated: 6/4/2025, 9:18:40 PM
class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        # Combine names and heights into a list of tuples
        people = list(zip(names, heights))
        
        # Sort the list of tuples by height in descending order
        sorted_people = sorted(people, key=lambda x: x[1], reverse=True)
        
        # Extract the names from the sorted list
        sorted_names = [person[0] for person in sorted_people]
        
        return sorted_names

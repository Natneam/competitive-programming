# LINK TO THE PROBLEM => https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        hashMap = dict()
        for i in employees:
            hashMap[i.id] = i
        process = [hashMap[id]]
        totalImportance = 0
        index = 0
        while index < len(process):
            employee = process[index]
            totalImportance += employee.importance
            for i in employee.subordinates:
                process.append(hashMap[i])            
            index += 1
        return totalImportance
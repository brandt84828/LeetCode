#1
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = collections.Counter(students)
        n, k = len(students), 0
        while k < n and count[sandwiches[k]]:
            count[sandwiches[k]] -= 1
            k += 1
        return n - k

#2
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while students and students.count(sandwiches[0]) != 0:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0) 
            else:
                students.append(students.pop(0))
        return len(students)
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = 0
        while sandwiches:
            if students[0] == sandwiches[0]:
                students = students[1:]
                sandwiches = sandwiches[1:]
                counter = 0
            else:
                students = students[1:] + students[:1]
                counter += 1
            if counter >= len(students):
                break
        return len(sandwiches)
        

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def output_job_description(self):
        print(f"{self.name}: General Employee")

    def output_earning(self):
        print(f"Earnings: {self.salary}")

class Janitor(Employee):
    def output_job_description(self):
        print(f"{self.name}: Maintains cleanliness of the facility")

class Programmer(Employee):
    def __init__(self, name, salary, bugs_fixed, bugs_created):
        super().__init__(name, salary)
        self.bugs_fixed = bugs_fixed
        self.bugs_created = bugs_created

    def output_job_description(self):
        print(f"{self.name}: Writes and debugs code. Bugs Fixed: {self.bugs_fixed}, Bugs Created: {self.bugs_created}")

class CEO(Employee):
    def __init__(self, name, salary, annual_bonus):
        super().__init__(name, salary)
        self.annual_bonus = annual_bonus

    def output_job_description(self):
        print(f"{self.name}: Oversees the entire organization. Annual Bonus: {self.annual_bonus}")

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, employee):
        self.heap.append(employee)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index].salary > self.heap[parent_index].salary:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left].salary > self.heap[largest].salary:
            largest = left
        if right < len(self.heap) and self.heap[right].salary > self.heap[largest].salary:
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

if __name__ == "__main__":
    heap = MaxHeap()
    employees = [
        Janitor("John", 30000),
        Programmer("Alice", 80000, 150, 50),
        CEO("Bob", 150000, 30000),
        Employee("Charlie", 40000),
        Programmer("Dave", 90000, 200, 60),
        CEO("Eve", 200000, 50000),
        Janitor("Frank", 32000),
        Employee("Grace", 45000),
        Programmer("Hank", 100000, 250, 70),
        CEO("Ivy", 250000, 70000)
    ]
    for emp in employees:
        heap.insert(emp)

    while True:
        employee = heap.extract_max()
        if employee is None:
            break
        employee.output_job_description()
        employee.output_earning()

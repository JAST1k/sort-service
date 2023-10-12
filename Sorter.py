class Sorter:

    def bubble_sort(self, list_of_numbers):
        for i in range(len(list_of_numbers)):
            for j in range(len(list_of_numbers) - 1):
                if list_of_numbers[j] > list_of_numbers[j + 1]:
                    list_of_numbers[j], list_of_numbers[j + 1] = list_of_numbers[j + 1], list_of_numbers[j]
        return list_of_numbers

    def min_index(self, list_of_numbers):
        min_index = 0
        for i in range(len(list_of_numbers)):
            if list_of_numbers[min_index] > list_of_numbers[i]:
                list_of_numbers[min_index] = list_of_numbers[i]

    def choise_sort(self, list_of_numbers):
        for i in range(len(list_of_numbers)):
            minimum = self.min_index(list_of_numbers[i])
            list_of_numbers[minimum + i], list_of_numbers[i] = list_of_numbers[i], list_of_numbers[minimum + i]
        return list_of_numbers

    def insert_sort(self, list_of_numbers):
        for i in range(len(list_of_numbers)):
            for j in range(len(list_of_numbers)):
                if list_of_numbers[j] > list_of_numbers[j + 1]:
                    list_of_numbers[j], list_of_numbers[j + 1] = list_of_numbers[j + 1], list_of_numbers[j]
        return list_of_numbers

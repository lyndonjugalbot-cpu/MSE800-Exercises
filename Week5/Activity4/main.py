import numpy
#Exercise for Dictionary comprehensions

def main():
    keys = [1, 'b', 'c', 'd', 'e']
    values = ['a', 2, 3, 4]
    dictionary = {k: v for k, v in zip(keys, values)}

    print(f"Answer: {dictionary}")
    print("***" *50)

    #merging dictionary
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    merged_dict = {**dict1, **dict2}
    print(f"Merge Dictionary: {merged_dict}")
    print("***" *50)

    #merging multiple dictionary
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    dict3 = {'d': 5, 'e': 6}
    merged_dict = {**dict1, **dict2, **dict3}
    print(f"Merge Multiple Dictionaries: {merged_dict}")
    print("***" *50)

    #Conditional Merging
    key1 = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'e', 'a']
    value1 = [20, 3, 1, 88, 55, 92, 6, 90, 910]
    key2 = ['u', 'b', 'o', 'x', 'e', 'a']
    value2 = [200, 30, 10, 88, 55, 920]

    dict1 = {k: v for k, v in zip(key1, value1)}
    dict2 = {k: v for k, v in zip(key2, value2)}

    merged_dict = {**{k: v for k, v in dict1.items() if v % 2 != 0},
                   **{k: v for k, v in dict2.items() if v % 2 != 0}
                  }
    print(f"Conditional Merging: {merged_dict}")
    print("***" *50)


    # extract information with age greater than 25 from the following list of dictionaries
    data1 = [{"name": "Alice", "age": 28}, {"name": "Bob", "age": 24}, {"name": "Charlie", "age": 30}]
    result = [d for d in data1 if d["age"] > 25]
    # [{'name': 'Alice', 'age': 28}, {'name': 'Charlie', 'age': 30}]
    print(f"Age greater than 25: {result}")


   
    # use list comprehension to flatten the matrix
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flat = [num for row in matrix for num in row]
    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Flattened matrix using numpy: {flat}")
   



    # use enumerate() for looping to add 5 extra point to each grade in the list, the 5th one add 10
    grades = [88, 92, 78, 65, 50, 94]
    adjusted = []
    for i, grade in enumerate(grades):
        adjusted.append(grade + 10 if i == 4 else grade + 5)
    # [93, 97, 83, 70, 60, 99]
    print(f"Adjusted grades: {adjusted}")



    # filter out elements depend on their index: 
    # use list comprehension and enumerate() to get elements with even index
    data = [100, 200, 300, 400, 500]
    even = []
    for i, dat1 in enumerate(data):
        if dat1 % 2 == 0:
            even.append(dat1)
    print(f"Even Indexes: {even}")


    # create a dictionary from lists using zip()
    keys = ['name', 'age', 'grade']
    values = ['Alice', 25, 'A']
    person_dict = {k: v for k, v in zip(keys, values)}
    print(f"Person Dictionary: {person_dict}")


    








if __name__ == "__main__":
    main()
# a python program to convert the elements of two lists into key-value pairs of a dictionary:
if __name__ =="__main__":
    # take two separate lists with elements:
    countries=["USA", "China", "India", "Japan", "Russia", "Germany", "France"]
    cities=["Washington", "Beijing", "New Delhi", "Tokyo", "Moscow", "Berlin", "Paris"]
    # make a dictionary:
    z=zip(countries, cities)
    d=dict(z)
    print(d) # Output: {'USA': 'Washington', 'China': 'Beijing', 'India': 'New Delhi', 'Japan': 'Tokyo', 'Russia': 'Moscow', 'Germany': 'Berlin', 'France': 'Paris'}
    # display key-value pairs from dictionary d:
    print("{:15s}--{:15s}".format("COUNTRY", "CAPITAL"))
    for k in d:
        print("{:15s}--{:15s}".format(k, d[k]))
def first_marker(datastream_buffer, characters):
    for i in range(characters,len(datastream_buffer)):
        string = datastream_buffer[(i - characters) : i]
        
        if not [s for s in string if string.count(s) > 1]:
            return i
            

with open('input.txt', 'r') as inp:
    datastream_buffer = inp.read()
            
    print(first_marker(datastream_buffer, 4))
    print(first_marker(datastream_buffer, 14))
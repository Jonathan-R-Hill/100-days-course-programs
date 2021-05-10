import pandas

data = pandas.read_csv("squirrel.CSV")

grey_sq = len(data[data["Primary Fur Color"] == "Gray"])
cinn_sq = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_sq = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Colours" : ["Gray", "Cinnamon", "Black"],
    "Amount" : [grey_sq, cinn_sq, black_sq]
}

my_data_frame = pandas.DataFrame(data_dict)
print(my_data_frame)


def first_go_storage():     # it worked but it's long
    data = pandas.read_csv("squirrel.CSV")
    
    fur_colour = data["Primary Fur Color"]

    gray = []
    cinn = []
    black = []
    for i in fur_colour:
        if i == "Gray":
            gray.append(i)
            
        elif i == "Cinnamon":
            cinn.append(i)
        
        elif i == "Black":
            black.append(i)

    data_dict = {
        "Colours" : ["Gray", "Cinnamon", "Black"],
        "Amount" : [len(gray), len(cinn), len(black)]
    }

    my_data_frame = pandas.DataFrame(data_dict)
    print(my_data_frame)
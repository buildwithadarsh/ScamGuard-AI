import pandas as pd

data = {
    "email": [
        "Congratulations! you have won a free vacation. click now!!!",
        "Hi team!, please find the updated attached document."
    ]
}

data_frame = pd.DataFrame(data)
print(data_frame)
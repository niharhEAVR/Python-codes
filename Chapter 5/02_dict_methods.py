marks = { 
    "name": "Nihar Debnath", 
    "marks": "45", 
    "out of": "100", 
    "id": [13, 223, 97],
    10: "progress"
} 

print("\n",marks.items())
print("\n",marks.keys())
print("\n",marks.values())
marks.update({10: "wait for recheck", "check":"sorry we cant pass you"})
print("\n",marks[10])
print("\n",marks.items())

print("\n",marks.get("name"))
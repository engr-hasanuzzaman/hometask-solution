single_level_dict = { "name": "Hasan", "age": 29, "passion": "programming"}
second_level_dict = { 
  "name": "Hasan", 
  "age": 29, 
  "passion": "programming",
  "address": { "district": "bogura", "country": "Bangladesh"}
  }

third_level_dict = { 
  "name": "Hasan", 
  "age": 29, 
  "passion": "programming",
  "address": { "district": "bogura", "country": "Bangladesh"},
  "parents": { 
    "father": { "fName": "Senior Hasa", "fAge": 49 },
    "mother": { "mName": "Hasan", "mAge": 29, "mProfession": "housewife"}
  }
}
# [["name", 1], ["age", 1], ["passion", 1], ["address", 1], ["parents", 1], ["district", 2], ["country", 2], ["father", 2], ["mother", 2], ["fName", 3], ["fAge", 3], ["mName", 3], ["mAge", 3], ["mProfession", 3]]
original_dict = {
  "key1": 1,
  "key2": {
    "key3": 1,
    "key4": {
      "key5": 4
    }
  }
}

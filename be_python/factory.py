#===========================================
# contains objects used for testing purposes
# ==========================================

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
tenth_level_dict = {
  "key1": {
    "key2": {
      "key3": {
        "key4": {
          "key5": {
            "key6": {
              "key7": {
                "key8": {
                  "key9":{
                    "key10": "final data"
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}

original_dict = {
  "key1": 1,
  "key2": {
    "key3": 1,
    "key4": {
      "key5": 4
    }
  }
}

# sample python object
class Person(object):
  def __init__(self, first_name, last_name, father):
    self.first_name = first_name
    self.last_name = last_name
    self.father = father

gFathe = Person("User", "1", None)
father = Person("User", "2", gFathe)
person = Person("User", "2", father)

dict_with_2nd_lev_object = {
      "key1": 1,
      "key2": {
        "key3": 1,
        "key4": {
          "key5": 4,
          "user": father,
        }
      },
}

dict_with_3rd_lev_object = {
      "key1": 1,
      "key2": {
        "key3": 1,
        "key4": {
          "key5": 4,
          "user": person,
        }
      },
}